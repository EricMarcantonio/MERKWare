
class Cipher:
    key: str = None
    byte_array: bytearray = None

    def xor_bytes(self, w: bytearray, x: bytearray):
        return bytearray(i ^ j for i, j in zip(w, x))

    def __init__(self, byte_array: bytearray, key: str):
        self.key = key
        self.byte_array = byte_array

    def encrypt(self) -> bytearray:
        while len(self.key) < len(self.byte_array):
            self.key *= 2
        return self.xor_bytes(self.byte_array, bytearray(self.key, encoding="utf-8"))
