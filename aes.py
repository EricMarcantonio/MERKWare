block = [[], [], [], []]

'''
Using a with statement autocloses the file after opening
the "rb" means to open the file for reading only, and open it in binary mode
'''
with open("./test_files/pic.txt", "rb") as f:
    #  f.read(16) takes the first 16 bytes
    byte = f.read(16)

    # byte will be b"" at the end, meaning its empty or reached EOF
    while byte:
        #converts to a hexstring. each byte is a 2 char hexadecimal
        hex_byte = byte.hex()
        '''
        AES uses a 4x4 matrix. This fills it in. I purposly did not use a for loop because
        it is easier to understand how this works, without figuring out the loop logic.
        '''
        block[0] = [hex_byte[0:2], hex_byte[2:4], hex_byte[4:6], hex_byte[6:8]]
        block[1] = [hex_byte[8:10], hex_byte[10:12], hex_byte[12:14], hex_byte[14:16]]
        block[2] = [hex_byte[16:18], hex_byte[18:20], hex_byte[20:22], hex_byte[22:24]]
        block[3] = [hex_byte[24:26], hex_byte[26:28], hex_byte[28:30], hex_byte[30:32]]

        #in case the file is less then 16 bytes (i.e a text file that has like 1 word)
        for i in range(0,4):
            for j in range(0,4):
                if(block[i][j] == ""):
                    block[i][j] = "00"

        print(hex_byte)
        print(block)

        #reset byte to be the NEXT 16 bytes (something not explicit)
        byte = f.read(16)

