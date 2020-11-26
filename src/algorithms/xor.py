from Crypto.Cipher.XOR import XORCipher


class Cipher:
    key: str = None
    obj: XORCipher = None

    def __init__(self, key: str):
        self.key = key
        self.obj = XORCipher(key)

    def encrypt(self, cipher: bytearray) -> bytes:
        return self.obj.encrypt(cipher)

    def decrypt(self, cipher: bytearray) -> bytes:
        return self.obj.decrypt(cipher)
