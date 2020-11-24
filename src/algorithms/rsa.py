import os
import ast

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from .rsa_utils import rsa_aes

class Cipher:
    rand_bytes = None
    key_name = ""

    def __init__(self, key_name: str):
        self.key_name = key_name
        self.generate_key_pair(4096)

    def encrypt(self,cipher_bytes: bytes) -> bytes:
        self.gen_random_bytes()
        print(self.rand_bytes)
        cipher = rsa_aes.Cipher(self.rand_bytes)
        
        encryptedFile =  cipher.encrypt(cipher_bytes)

        result = bytearray(encryptedFile)
        result.append(self.encryption_tail())
        return result

    def decrypt(self,cipher_bytes: bytes) -> bytes:
        tail = cipher_bytes[-256:]
        cipherBytes = cipher_bytes[:-256]

        key = self.decrypt_tail(tail) 
        cipher = rsa_aes.Cipher(key)
        
        result = cipher.encrypt(cipherBytes)
        return result


    def encryption_tail(self) -> bytes:
        public_key = open(self.key_name + "_pub.pem", "rb")
        pub = RSA.importKey(public_key.read())
        public_key.close()

        encryptor = PKCS1_OAEP.new(pub)
        encrypted = encryptor.encrypt(self.rand_bytes)

        return encrypted


    def decrypt_tail(self,byte_array: bytes) -> bytes:
        private_key = open(self.key_name + ".pem", "rb")
        priv = RSA.importKey(private_key.read())
        private_key.close()

        decryptor = PKCS1_OAEP.new(priv)
        decrypted = decryptor.decrypt(byte_array)

        return decrypted


    def generate_key_pair(self,bit_size: int) -> None:
        key = RSA.generate(bit_size)
        pub = key.publickey()

        f = open(self.key_name + "_pub.pem", "wb")
        f.write(pub.export_key())
        f.close()
        print("GENERATED PUBLIC KEY: ", self.key_name + "_pub.pem")
        f = open(self.key_name + ".pem", "wb")
        f.write(key.export_key())
        f.close()
        print("GENERATED PRIVATE KEY: ", self.key_name + ".pem")

    def gen_random_bytes(self) -> bytes:
        self.rand_bytes = os.urandom(256)



if __name__ == '__main__':
    rsa = Cipher("test")
    rsa.gen_random_bytes() 
    rsa.generate_key_pair(4096)
    encrypted = rsa.encryption_tail()
    decrypted = rsa.decrypt_tail(encrypted)
    assert rsa.rand_bytes == decrypted
    print(rsa.rand_bytes == decrypted)


'''
This file generates a public and a private key pair.

This public and private key pair is meant to encrypt and decrypt a string

AES should be used to actually encrypt the file (in order to encrypt more than 256 bytes)

STEPS:
    1. Generate a public private key pair

ENCRYPTION
    2. Generate random bytes of length n (os.urandom(n = 256))
    3. use these bytes to encrypt the file
    4. Use the public key to encrypt the random bytes
    5. append the encrypted random bytes to the end of the AES encrypted file
    6. DONE

DECRYPTION
    7. remove the last n bytes from the encrypted file and decrypt these bytes with the private key
    8. Decrypt the file using AES and the decrypted key
    9. DONE
'''
