import sys
import argparse

# Sample algorithm module import
# from algorithms.Asymmetric import algo1
# from algorithms.Symmetric import algo2
# from algorithms.Symmetric import aes

# a = aes.AES()
# a1 = algo1.Algo1('Init String 1')
# a2 = algo2.Algo2('Init String 2')

# a1.print()
# a2.print()


# ARGUMENT PARSER
# Make all of these required when modules are fully implemented
args = argparse.ArgumentParser()

args.add_argument("-f","--folder", required=False, help="Folder that will be encrypted/decrypted")
args.add_argument("-t","--type", required=False, help="Algorithm type selection")
args.add_argument("-s","--secrets", required=False, help="An n-tuple input used for key secrets and other parameters")
args.add_argument("-a","--action", required=False, help="Encrypt or decrypt folder")

args_dict = vars(args.parse_args())
print('COMMAND LINE ARGUMENTS: ', args_dict)

print("Exiting...")

