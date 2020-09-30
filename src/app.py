import sys
import argparse

from algos import algo1
from algos import algo2

args = argparse.ArgumentParser()

a1 = algo1.Algo1('Init String 1')
a2 = algo2.Algo2('Init String 2')

a1.print()
a2.print()

# Make all of these required when modules are fully implemented
args.add_argument("-f","--folder", required=False, help="Folder that will be encrypted/decrypted")
args.add_argument("-t","--type", required=False, help="Algorithm type selection")
args.add_argument("-s","--secrets", required=False, help="n-tuple input used for key secrets and other parameters")
args.add_argument("-a","--action", required=False, help="encrypt or decrypt")

args_dict = vars(args.parse_args())

print('COMMAND LINE ARGUMENTS: ', args_dict)

