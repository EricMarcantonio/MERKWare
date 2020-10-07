from typing import List, Any, Union


class RC4:
    __author__ = "Moreka Kazemi"
    __copyright__ = "Copyright 2020, The MERKware group"

    def __init__(self, key, length=256):
        self.length = length
        self.s = list(range(0, self.length))
        self.keystream = []
        # Making the key as the same length as the length
        self.key = (self.key_polishing(key) * (int(length / len(str(key))) + 1))[:length]

    @staticmethod
    def key_polishing(key):
        try:
            # Converting the string key into a list of integers
            if type(key) == str:
                return list(map(int, list(key)))
            # Making sure the key list is integer
            elif type(key) == list:
                return list(map(int, key))
            # Converting an integer into a key list
            elif type(key) == int:
                return list(map(int, list(str(key))))
            else:
                raise Exception("I'm gonna go ahead and assume your key won't work")
        except Exception as e:
            print("Key is not acceptable:", str(e))

    def key_scheduling(self):
        self.s = list(range(0, self.length))
        j = 0
        for i in range(0, self.length):
            j = (j + self.s[i] + self.key[i]) % self.length
            self.s[i], self.s[j] = self.s[j], self.s[i]

        print(self.s)
        print(self.key)

    def pseudo_random(self, text):
        j = 0
        self.keystream = []
        for i in range(1, len(text) + 1):
            j = (j + self.s[i]) % self.length
            self.s[i], self.s[j] = self.s[j], self.s[i]
            t = (self.s[i] + self.s[j]) % self.length
            self.keystream.append(self.s[t])

        print('keystream', self.keystream)

    def encrypt(self, plaintext):
        self.key_scheduling()
        self.pseudo_random(plaintext)

        # keystream XOR plaintext
        return [x ^ int(bytes(y.encode())) for x, y in zip(self.keystream, list(plaintext))]

    def decrypt(self, cipher):
        self.key_scheduling()
        self.pseudo_random(cipher)
        # return [x ^ y for x, y in zip(self.keystream, list(bytes(cipher.encode())))]
        return [x ^ int(bytes(y.encode())) for x, y in zip(self.keystream, list(cipher))]

rc4 = RC4(key=31415, length=8)
cipher = rc4.encrypt(['6', '1', '5', '4'])
cipher = list(map(str, cipher))
print('cipher', cipher)

print('-----------')

text = rc4.decrypt(cipher)
print('text', text)
