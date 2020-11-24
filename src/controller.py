from utils import file_utils
from algorithms import aes, rc4, xor, rsa

def encrypt_file(cipher: str, file_path : str, key: str):

    fileBytes = file_utils.read_file(file_path)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(key)
    # Bytes to write to modified file
    if algo:
        # encrypt zipped folder
        print("ENCRYPTING FILE BYTES",'\n')
        newBytes = bytes(algo.encrypt(bytes(fileBytes)))
        # write encrypted bytes and rename zip 
        file_utils.write_file(file_path,newBytes)
        MERKed_file = file_utils.merk(file_path)
        print(f"{file_path} has been MERKed:",MERKed_file)

def decrypt_file(cipher: str, file_path : str, key: str):
    clean_file = file_utils.unmerk(file_path)
    
    fileBytes = file_utils.read_file(clean_file)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(key)
    # Bytes to write to modified file
    if algo:
        # decrypt zipped folder
        print("DECRYPTING FILE BYTES",'\n')
        newBytes = bytes(algo.decrypt(bytes(fileBytes)))
        # write encrypted bytes and rename zip 
        file_utils.write_file(clean_file,newBytes)
        print(f"{clean_file} has been unMERKed")

def encrypt_folder(cipher: str, folder_path : str, key: str):
    # Create new zip and delete old folder
    oldFolder, newZip = file_utils.zip_folder(folder_path)
    file_utils.delete_folder(oldFolder)

    fileBytes = file_utils.read_file(newZip)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(key)
    # Bytes to write to modified file
    if algo:
        # encrypt zipped folder
        newBytes = bytes(algo.encrypt(bytes(fileBytes)))
        # write encrypted bytes and rename zip 
        file_utils.write_file(newZip,newBytes)
        MERKed_file = file_utils.merk(newZip)
        print(f"{folder_path} has been MERKed:",MERKed_file)

def decrypt_folder(cipher: str, folder_path : str, key: str):
    clean_file = file_utils.unmerk(folder_path)
    
    fileBytes = file_utils.read_file(clean_file)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(key)
    # Bytes to write to modified file
    if algo:
        # decrypt zipped folder
        newBytes = bytes(algo.decrypt(bytes(fileBytes)))
        # write encrypted bytes and rename zip 
        file_utils.write_file(clean_file,newBytes)
    unzippedFile = file_utils.unzip_folder(clean_file)
    file_utils.delete_file(clean_file)
    print(f"{clean_file} has been unMERKed")

def mux(choice: str):
    algos = {
        'aes': aes,
        'xor': xor,
        'rc4': rc4,
        'rsa': rsa
    }
    if choice in algos.keys():
        return algos[choice]
    return None
