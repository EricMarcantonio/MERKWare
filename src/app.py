import sys
from os.path import isdir, join, abspath
import argparse
import shutil

# A boolean that turns on/off debug mode.
DEBUG = False

# ARGUMENT PARSER
# Make all of these required when modules are fully implemented
args = argparse.ArgumentParser()

# Forcing the user to enter all the parameters in production mode
# Skipping this in debug mode
parameter_required = False if DEBUG else True

args.add_argument("-f", "--folder", required=parameter_required, help="Folder that will be encrypted/decrypted")
args.add_argument("-t", "--type", required=parameter_required, help="Algorithm type selection")
args.add_argument("-s", "--secrets", required=False,
                  help="An n-tuple input used for key secrets and other parameters")
args.add_argument("-a", "--action", required=parameter_required, help="Encrypt or decrypt folder")

args_dict = vars(args.parse_args())
folder_path = abspath(args_dict['folder'])
action = args_dict['action']
cipher = args_dict['type']

key = args_dict['secrets']

from controller import encrypt, decrypt

if action == 'encrypt':
    encrypt(cipher,folder_path,key) # folder path and key for encryption
elif action == 'decrypt':
    decrypt(cipher,folder_path,key)
else:
    print('Invalid Action, choose decrypt or encrypt\n')
