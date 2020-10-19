from Crypto.Cipher import AES as aes


def fix_key_length(k: bytes) -> bytes:
    if len(k) < 16:
        temp = bytearray(k)
        while len(temp) < 16:
            temp.append(0x00)
        return bytes(temp)
    elif len(k) == 16:
        return k
    elif len(k) < 24:
        return k[0:16]
    elif len(k) == 24:
        return k
    elif len(k) < 32:
        return k[0:24]
    elif len(k) == 32:
        return k
    else:
        return k[0:32]


class AES:
    cipher_block: aes.AESCipher = None
    master_key: bytes = None
    bytes_to_crypt: bytes = None

    def __init__(self, master_key: bytearray, bytes_to_encrypt: bytearray) -> None:
        self.master_key = fix_key_length(bytes(master_key))
        self.cipher_block = aes.new(self.master_key, aes.MODE_CFB, "This is an IV456")
        self.bytes_to_crypt = bytes(bytes_to_encrypt)

    def encrypt(self) -> bytearray:
        return bytearray(self.cipher_block.encrypt(self.bytes_to_crypt))

    def decrypt(self) -> bytearray:
        return bytearray(self.cipher_block.decrypt(self.bytes_to_crypt))


message = bytearray("The answer is n", encoding="utf-8")
key = bytearray("Hello World 123", encoding="utf-8")
test = AES(key, message)
encrypted_msg = test.encrypt()

decrypt = AES(key, encrypted_msg)
print(decrypt.decrypt())
