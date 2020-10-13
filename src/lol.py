a = [0x65, 0x66]
b = [0x67, 0x68]

tf = bytes(i ^ j for i, j in zip(a, b))
print(tf[1:2])

a = bytearray("password", encoding="utf-8")
