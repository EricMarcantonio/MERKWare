
import sys


from hello import say_info

print(sys.argv)

s = say_info("Hello")

print(s.get_info())

def print_hello():
    print("Hello World!")