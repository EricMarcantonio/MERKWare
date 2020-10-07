import os
import shutil
import time




class File:
    is_dir = None
    parent_folder = None
    file_path_raw = None
    file_name = None
    file_read_zipped = None
    file_write_encrypted = None

    def __init__(self, file_name_with_path: str):
        if os.path.isfile(file_name_with_path):
            self.is_dir = False
            self.file_path_raw = os.path.abspath(file_name_with_path)
            self.file_name = self.file_path_raw[self.file_path_raw.rfind("/") + 1: len(self.file_path_raw)]
            self.parent_folder = self.file_path_raw[0:self.file_path_raw.rfind("/")]
        elif os.path.isdir(file_name_with_path):
            self.is_dir = True
            self.file_path_raw = os.path.abspath(file_name_with_path)
            self.file_name = self.file_path_raw[self.file_path_raw.rfind("/") + 1: len(self.file_path_raw)]
            self.parent_folder = self.file_path_raw[0:self.file_path_raw.rfind("/")]
        else:
            raise FileNotFoundError()

    def zip_folder(self):
        # Make the
        shutil.make_archive(self.file_name, "zip", self.file_path_raw)
        shutil.move(self.file_name + ".zip", self.parent_folder)
        self.file_read_zipped = open(self.file_path_raw + ".zip", "rb")
        # self.file_write_encrypted = open(self.file_path_raw + ".merk", "wb")
        shutil.rmtree(self.file_path_raw)

    def unzip_folder(self):
        shutil.unpack_archive(self.file_path_raw, self.parent_folder, "zip")


file = File("../../spec/test_files")
file.zip_folder()

# file.zip_file()
