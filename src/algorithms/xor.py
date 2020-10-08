import os

from src.utils.data_management import File, Folder


def xor_bytes(w, x):
    return bytes(i ^ j for i, j in zip(w, x))


class XOR:
    file: File or Folder = None
    key: str = None
    new_file: File or Folder = None

    def __init__(self, filename: str, key: str):
        self.key = key
        if os.path.exists(filename):
            if os.path.isdir(filename):
                self.file = Folder(filename)
                self.file.zip_folder()
                self.file = File(self.file.folder_zipped_name)

            if os.path.isfile(filename):
                self.file = File(filename)
                if not self.file.file_path_raw.endswith(".merk"):
                    self.new_file = self.file.encrypted_file_stream()
                else:
                    self.new_file = self.file.decrypted_file_stream()
            else:
                raise FileNotFoundError
        else:
            raise FileExistsError

    def crypt(self):
        total_bytes = self.file.read_file().read()
        while len(bytes(self.key, encoding='ascii')) < len(total_bytes):
            self.key *= 2
        key_bytes = bytes(self.key, encoding='ascii')
        self.new_file.write(xor_bytes(total_bytes, key_bytes))
        self.file.delete()
        name_wo_merk = self.file.file_name[0:self.file.file_name.rfind(".")]
        # if name_wo_merk.endswith("zip"):
