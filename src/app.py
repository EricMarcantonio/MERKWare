import sys
from os.path import isdir
import argparse
import shutil
from algorithms.aes import AES

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

print('COMMAND LINE ARGUMENTS: ', args_dict)
print(list(args_dict.values()))

# is the folder accessible?
if isdir(args_dict['folder']):
    # AES Encrypt and zip (NEED TO REMOVE AND REPLACE WITH ALGO MULTIPLEXER)
    zipped = shutil.make_archive("test", "zip", args_dict['folder'])
    AES(zipped)
    shutil.unpack_archive("test.zip", "./", None)
else:
    print("NOT A DIR OR FILE")

print("Exiting...")
