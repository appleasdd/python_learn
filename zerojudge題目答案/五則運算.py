import sys
while True:
    try:
        x = input()
        print(eval(x))
    except EOFError:
        break
