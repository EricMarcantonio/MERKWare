from utils import file_utils
from algorithms import aes, lib_aes, rc4, xor

def encrypt(cipher: str, folder_path : str, key: str):
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

def decrypt(cipher: str, folder_path : str, key: str):
    clean_file = file_utils.unmerk(folder_path)
    
    fileBytes = file_utils.read_file(clean_file)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(key)
    # Bytes to write to modified file
    if algo:
        # encrypt zipped folder
        newBytes = bytes(algo.decrypt(bytes(fileBytes)))
        # write encrypted bytes and rename zip 
        file_utils.write_file(clean_file,newBytes)
    unzippedFile = file_utils.unzip_folder(clean_file)
    file_utils.delete_file(clean_file)
    print(f"{clean_file} has been unMERKed")

def mux(choice: str):
    algos = {
        'aes': lib_aes,
        'xor': xor,
        'rc4': rc4
    }
    if choice in algos.keys():
        return algos[choice]
    return None
