def xor_bytes(w: bytearray, x: bytearray):
    return bytearray(i ^ j for i, j in zip(w, x))


class XOR:
    key: str = None
    byte_array: bytearray = None

    def __init__(self, byte_array: bytearray, key: str):
        self.key = key
        self.byte_array = byte_array

    def crypt(self) -> bytearray:
        while len(self.key) < len(self.byte_array):
            self.key *= 2
        return xor_bytes(self.byte_array, bytearray(self.key, encoding="utf-8"))
