import os
import shutil


class File:
    parent_folder = None
    file_path_raw = None
    file_name = None
    file_read_stream = None
    file_write_encrypted = None
    file_write_decrypted = None
    starting_dir = None

    def __init__(self, file_name: str):
        if os.path.isfile(file_name):
            self.starting_dir = os.getcwd()
            self.file_path_raw = os.path.abspath(file_name)
            self.file_name = self.file_path_raw[self.file_path_raw.rfind("/") + 1: len(self.file_path_raw)]
            self.parent_folder = self.file_path_raw[0:self.file_path_raw.rfind("/")]
        else:
            raise FileNotFoundError()

    def read_file(self):
        self.file_read_stream = open(self.file_path_raw, "rb")
        return self.file_read_stream

    def encrypted_file_stream(self):
        self.file_write_encrypted = open(self.file_path_raw + '.merk', "wb")
        return self.file_write_encrypted

    def decrypted_file_stream(self):
        self.file_write_decrypted = open(self.file_path_raw[0:self.file_path_raw.rfind(".")], "wb")
        return self.file_write_decrypted

    def delete(self):
        os.remove(self.file_path_raw)

    def unzip_folder(self):
        os.chdir(self.parent_folder)
        shutil.unpack_archive(filename=self.file_name)


class Folder:
    starting_folder = None
    parent_folder = None
    folder_path_raw = None
    folder_name = None
    folder_zipped_read_stream = None
    folder_zipped_write_encrypted = None
    folder_zipped_name = None

    def __init__(self, folder_name):
        if os.path.isdir(folder_name):
            self.starting_folder = os.getcwd()
            self.folder_path_raw = os.path.abspath(folder_name)
            self.folder_name = self.folder_path_raw[self.folder_path_raw.rfind("/") + 1: len(self.folder_path_raw)]
            self.parent_folder = self.folder_path_raw[0:self.folder_path_raw.rfind("/")]
        else:
            raise FileNotFoundError

    def zip_folder(self):
        os.chdir(self.parent_folder)
        shutil.make_archive(base_name=self.folder_name, format="zip",
                            base_dir=self.folder_name)
        os.chdir(self.starting_folder)

    def delete(self):
        shutil.rmtree(self.folder_path_raw)

    def unzip_folder(self):
        os.chdir(self.parent_folder)
        shutil.unpack_archive(filename=self.folder_name)


# --------------TESTING-------------------
folder = Folder("../../spec/test_files")
folder.zip_folder()
folder.delete()

folder = File("../../spec/test_files.zip")
# There are just tests below
folder.encrypted_file_stream()
folder.delete()

'''
The idea is to zip a folder and then open that folder as a file.
1. Zip the folder by invoking method
2. Delete the dir by invoking method
3. Make a new File object (I overwrote the old one), with the .zip as the file
4. In the code above, I have created a new file with a .merk extension. You would write the encrypted contents
to this
5. Delete the old zip file, after encrpting it

Note: you can open a stream to the zip file by using File.read_file() You can edit the .merk file by getting the stream from File.encrypted_file_stream()

At the moment this overwrites the testing folder so use the methods to not have to make a folder manually everytime. 
I have tested it so that it can zip a file and then open a stream to encrypt it. There is 0 encryption is this file, and it should stay like that.
the .merk allows you to write to a new file. Decrypt the file first and remove the .merk before feeding it into something.

'''
