from utils import file_utils
from algorithms import aes, rc4, xor

def encrypt(cipher: str, folder_path : str, key: str):

    # Create new zip and delete old folder
    oldFolder, newZip = file_utils.zip_folder(folder_path)
    file_utils.delete_folder(oldFolder)

    fileBytes = file_utils.read_file(newZip)
    # returns chosen cipher class
    algo = mux(cipher).Cipher(bytearray(fileBytes),key)
    # Bytes to write to modified file
    if algo:
        # encrypt zipped folder
        newBytes = bytes(algo.encrypt())
        # write encrypted bytes and rename zip 
        file_utils.write_file(newZip,newBytes)
        MERKed_file = file_utils.merk(newZip)
        print(MERKed_file)


def mux(choice: str):
    algos = {
        'aes': aes,
        'xor': xor,
        'rc4': rc4
    }
    if choice in algos.keys():
        return algos[choice]
    return None
