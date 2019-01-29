import os

base_path = os.path.dirname(os.path.abspath(__file__))
filename = base_path + '/pi_digits.txt'
with open('pi_digits.txt', encoding='utf-8') as file_object:
    lines = file_object.readlines()
    print(lines)
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
birthday = input('enter your birthday, in the form mmddyy:')
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appear in the first million digits of pi.")
print(pi_string)
print(len(pi_string))


