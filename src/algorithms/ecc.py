from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii


class ECC:
    def __init__(self, curve="brainpoolP256r1"):
        curve_options = ["brainpoolP160r1",
                         "brainpoolP192r1",
                         "brainpoolP224r1",
                         "brainpoolP256r1",
                         "brainpoolP320r1",
                         "brainpoolP384r1",
                         "brainpoolP512r1",
                         "secp192r1",
                         "secp224r1",
                         "secp256r1",
                         "secp384r1",
                         "secp521r1"]

        if curve in curve_options:
            self.curve = registry.get_curve(curve)
        else:
            raise Exception("the specified curve is unknown.")

    def get_public_key(self, privateKey):
        publicKey = privateKey * self.curve.g
        return publicKey

    def encrypt(self, msg, publicKey):
        ciphertextPrivateKey = secrets.randbelow(self.curve.field.n)
        sharedECCKey = ciphertextPrivateKey * publicKey
        sha = hashlib.sha256(int.to_bytes(sharedECCKey.x, 32, 'big'))
        sha.update(int.to_bytes(sharedECCKey.y, 32, 'big'))
        secretKey = sha.digest()
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        nonce = aesCipher.nonce
        ciphertextPublicKey = ciphertextPrivateKey * self.curve.g
        return (ciphertext, nonce, authTag, ciphertextPublicKey)

    def decrypt(self, ciphertext, nonce, authTag, ciphertextPublicKey, privateKey):
        sharedECCKey = privateKey * ciphertextPublicKey
        sha = hashlib.sha256(int.to_bytes(sharedECCKey.x, 32, 'big'))
        sha.update(int.to_bytes(sharedECCKey.y, 32, 'big'))
        secretKey = sha.digest()
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext


if __name__ == "__main__":
    ecc = ECC()

    msg = b'This is a test'
    print("original msg:", msg)
    privateKey = secrets.randbelow(0x321)
    publicKey = ecc.get_public_key(privateKey)

    ciphertext, nonce, authTag, ciphertextPubKey = ecc.encrypt(msg, publicKey)
    print("encrypted msg:", ciphertext)

    decryptedMsg = ecc.decrypt(ciphertext, nonce, authTag, ciphertextPubKey, privateKey)
    print("decrypted msg:", decryptedMsg)
