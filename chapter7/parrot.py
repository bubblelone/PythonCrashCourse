
promt = "\ntell me something,and i will repeat it back to you:"
promt += "\nEnter 'quit' to end the program."

active = True

while active :
    message = input(promt)

    if message == 'quit':
        active = False
    else:
        print(message)