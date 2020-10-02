class AES(str):
    file_name = ""
    

    def __init__(self, file_name: str):
        self.file_name = file_name

    
    def open_file(self, file_name: str)





four_by_four = [[], [], [], []]

'''
Using a with statement autocloses the file after opening
the "rb" means to open the file for reading only, and open it in binary mode
'''

file_read = open("test_files/GovSecrets.docx", "rb")
file_write = open("test_files/output/GovSecrets.docx.merk", "wb")



#  f.read(16) takes the first 16 bytes
byte = file_read.read(16)
# byte will be b"" at the end, meaning its empty or reached EOF
while byte:
    #converts to a hexstring. each byte is a 2 char hexadecimal
    hex_byte = byte.hex()
    hex_strings.append(hex_byte)
    
    '''
    AES uses a 4x4 matrix. This fills it in. I purposly did not use a for loop because
    it is easier to understand how this works, without figuring out the loop logic.

    
        b0, b4, b8, b12
        b1, b5, b9, b13
        b2, b6, b10, b14,
        b3, b7, b11, b15,
    
    '''
    four_by_four[0] = [hex_byte[0:2], hex_byte[8:10], hex_byte[16:18], hex_byte[24:26]]
    four_by_four[1] = [hex_byte[2:4], hex_byte[10:12], hex_byte[18:20], hex_byte[26:28]]
    four_by_four[2] = [hex_byte[4:6], hex_byte[12:14], hex_byte[20:22], hex_byte[28:30]]
    four_by_four[3] = [hex_byte[6:8], hex_byte[14:16], hex_byte[22:24], hex_byte[30:32]]

    #in case the file is less then 16 bytes (i.e a text file that has like 1 word)
    for i in range(0,4):
        for j in range(0,4):
            if(four_by_four[i][j] == ""):
                four_by_four[i][j] = "00"

    

    #reset byte to be the NEXT 16 bytes (something not explicit)
    byte = file_read.read(16)