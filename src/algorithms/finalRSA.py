import os
import ast

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt(byte_array: bytes, key_name: str) -> bytes:
    public_key = open(key_name + "_pub.pem", "rb")
    pub = RSA.importKey(public_key.read())
    public_key.close()

    encryptor = PKCS1_OAEP.new(pub)
    encrypted = encryptor.encrypt(byte_array)

    return encrypted


def decrypt(byte_array: bytes, key_name: str) -> bytes:
    private_key = open(key_name + ".pem", "rb")
    priv = RSA.importKey(private_key.read())
    private_key.close()

    decryptor = PKCS1_OAEP.new(priv)
    decrypted = decryptor.decrypt(byte_array)

    return decrypted


def generate_key_pair(bit_size: int, key_name: str) -> None:
    key = RSA.generate(bit_size)
    pub = key.publickey()

    f = open(key_name + "_pub.pem", "wb")
    f.write(pub.export_key())
    f.close()
    f = open(key_name + ".pem", "wb")
    f.write(key.export_key())
    f.close()


if __name__ == '__main__':
    rand = os.urandom(256)  # random string, generated from t
    generate_key_pair(4096, "test")
    encrypted = encrypt(rand, "test")
    decrypted = decrypt(encrypted, "test")
    assert rand == decrypted


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
