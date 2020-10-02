hex_strings = []


file_read = open("test_files/GovSecrets.docx", "rb")
file_write = open("test_files/output/GovSecrets.docx.merk", "w")

byte = file_read.read(16)
while byte:
    hex_byte = byte.hex()
    hex_strings.append(hex_byte)
    byte = file_read.read(16)

[file_write.write(eachLine + "\n") for eachLine in hex_strings]

file_read.close();
file_write.close();