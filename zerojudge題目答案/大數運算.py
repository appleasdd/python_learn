import sys
for i in sys.stdin:
    print(eval(i.replace("/", "//")))
while True:
    try:
        x = input()
        print(eval(x))
    except EOFError:
        break