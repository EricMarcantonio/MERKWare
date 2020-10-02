block = [[], [], [], []]

with open("./test_files/GovSecrets.docx", "rb") as f:
    byte = f.read(16)
    while byte:
        hex_byte = byte.hex()
        block[0] = [hex_byte[0:2], hex_byte[2:4], hex_byte[4:6], hex_byte[6:8]]
        block[1] = [hex_byte[8:10], hex_byte[10:12], hex_byte[12:14], hex_byte[14:16]]
        block[2] = [hex_byte[16:18], hex_byte[18:20], hex_byte[20:22], hex_byte[22:24]]
        block[3] = [hex_byte[24:26], hex_byte[26:28], hex_byte[28:30], hex_byte[30:32]]
        print(hex_byte)
        print(block)
        byte = f.read(16)
