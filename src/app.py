import sys
from os.path import isdir, join, abspath
import argparse
import shutil
from os import walk, getcwd

# A boolean that turns on/off debug mode.
DEBUG = True

# ARGUMENT PARSER
# Make all of these required when modules are fully implemented
args = argparse.ArgumentParser()

# Forcing the user to enter all the parameters in production mode
# Skipping this in debug mode
parameter_required = False if DEBUG else True

args.add_argument("-f", "--folder", required=parameter_required, help="Folder that will be encrypted/decrypted")
args.add_argument("-t", "--type", required=parameter_required, help="Algorithm type selection")
args.add_argument("-s", "--secrets", required=parameter_required,
                  help="An n-tuple input used for key secrets and other parameters")
args.add_argument("-a", "--action", required=parameter_required, help="Encrypt or decrypt folder")

args_dict = vars(args.parse_args())

curr_dir = getcwd()
folder_path = abspath(args_dict['folder'])

from utils.file_utils import zip_folder, delete_folder, read_file

oldFolder, newZip = (zip_folder(folder_path))
delete_folder(oldFolder)
fileBytes = read_file(newZip)

print(fileBytes)




