class Cipher:
    key: str = None

    def xor_bytes(self, w: bytearray, x: bytearray) -> bytes:
        return bytes(i ^ j for i, j in zip(w, x))

    def __init__(self, key: str):
        self.key = key

    def encrypt(self, cipher: bytearray) -> bytes:
        while len(self.key) < len(cipher):
            self.key *= 2
        return self.xor_bytes(cipher, bytearray(self.key, encoding="utf-8"))

    def decrypt(self, cipher: bytearray) -> bytes:
        while len(self.key) < len(cipher):
            self.key *= 2
        return self.xor_bytes(cipher, bytearray(self.key, encoding="utf-8"))
