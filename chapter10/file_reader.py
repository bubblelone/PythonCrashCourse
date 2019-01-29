import os

base_path = os.path.dirname(os.path.abspath(__file__))
filename = base_path + '/pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
