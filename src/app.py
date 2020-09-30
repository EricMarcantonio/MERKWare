import sys
import argparse

args = argparse.ArgumentParser()

args.add_argument("-f","--folder", required=True, help="Folder that will be encrypted/decrypted")
args.add_argument("-t","--type", required=True, help="Algorithm type selection")
args.add_argument("-s","--secrets", required=False, help="n-tuple input used for key secrets and other parameters")
args.add_argument("-a","--action", required=True, help="encrypt or decrypt")

args_dict = vars(args.parse_args())

print('COMMAND LINE ARGUMENTS: ' , args_dict)
