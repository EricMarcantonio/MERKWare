from tinyec import registry
import tinyec.ec as ec
from Crypto.Cipher import AES
import hashlib, secrets, binascii
import json
import base64

class Cipher:
    def __init__(self, curve="brainpoolP256r1"):
        if curve is "" or curve is None:
            self.curve = "brainpoolP256r1"

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
            raise Exception("the specified curve is unknown",curve)

    def get_public_key(self, privateKey):
        publicKey = privateKey * self.curve.g
        return publicKey

    def encrypt_helper(self, msg, publicKey):
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

    def decrypt_helper(self, ciphertext, nonce, authTag, ciphertextPublicKey, privateKey):
        sharedECCKey = privateKey * ciphertextPublicKey
        sha = hashlib.sha256(int.to_bytes(sharedECCKey.x, 32, 'big'))
        sha.update(int.to_bytes(sharedECCKey.y, 32, 'big'))
        secretKey = sha.digest()
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext

    def encrypt(self,cipher_bytes: bytes) -> bytes:
        privateKey = secrets.randbelow(0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7)
        publicKey = self.get_public_key(privateKey)

        ciphertext, nonce, authTag, ciphertextPubKey = self.encrypt_helper(cipher_bytes, publicKey)
        keyDump = {
            'nonce': (nonce).hex(),
            'authTag': (authTag).hex(),
            'x': int(ciphertextPubKey.x),
            'y': int(ciphertextPubKey.y),
            'privateKey': int(privateKey)
        }
        
        key_file = open("ecc_key.json",'w')
        json.dump(keyDump,key_file, indent=6)
        key_file.close()
        return ciphertext

    def decrypt(self,cipher_bytes: bytes) -> bytes:
        key_file = open("ecc_key.json",'r')
        keyDetails = json.load(key_file)
        key_file.close()
        nonce = bytes.fromhex(keyDetails['nonce'])
        authTag = bytes.fromhex(keyDetails['authTag'])

        print(nonce)

        ciphertextPubKey = ec.Point(self.curve, keyDetails['x'], keyDetails['y'])
        privateKey = int(keyDetails['privateKey'])

        decryptedMsg = self.decrypt_helper(cipher_bytes, nonce, authTag, ciphertextPubKey, privateKey)

        return decryptedMsg 


if __name__ == "__main__":
    ecc = Cipher()

    msg = b'This is a test'
    print("original msg:", msg)
    privateKey = secrets.randbelow(0xAAAAAAAAAAAAAAAAAAA)
    publicKey = ecc.get_public_key(privateKey)

    ciphertext, nonce, authTag, ciphertextPubKey = ecc.encrypt_helper(msg, publicKey)
    print("encrypted msg:", ciphertext)

    decryptedMsg = ecc.decrypt_helper(ciphertext, nonce, authTag, ciphertextPubKey, privateKey)
    print("decrypted msg:", decryptedMsg)

