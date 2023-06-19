from sys import stdin
import math
for x in stdin:
    def s(c,e):
        if c == 0:
            print(0)
        elif abs(c) == 1:
            print("-",abs(e),sep = "")
        elif abs(c) == abs(e):
            print("-",abs(e),sep = "")
        else:
            print("-",abs(e),"/",abs(c),sep = "")
    def v(c,e):
        if abs(c) == 0:
            print(0)
        elif abs(c) == 1:
            print(abs(e))
        elif abs(c) == abs(e):
            print(abs(e),sep = "")
        else:
            print(abs(e),"/",abs(c),sep = "")
    x = x.split(" ")
    b = x[4]
    x.pop(-1)
    x = list(map(int,x))
    a = int()
    c = int()
    d = int()
    f = int()
    if b == "+\n":
        c = x[1] * x[3]
        e = (x[3] * x[0]) + (x[2] * x[1])
        f = math.gcd(c,e)
        c = int(c//f)
        e = int(e//f)
        if bool(c < 0) ^ bool(e < 0):
            s(c,e)
        else:
            v(c,e)
    if b == "-\n":
        c = x[1] * x[3]
        e = (x[3] * x[0]) - (x[2] * x[1])
        f = math.gcd(c,e)
        c = int(c//f)
        e = int(e//f)
        if bool(c < 0) ^ bool(e < 0):
            s(c,e)
        else:
            v(c,e)
    if b == "*\n":
        c = x[1] * x[3]
        e = x[0] * x[2]
        f = math.gcd(c,e)
        c = int(c//f)
        e = int(e//f)
        if bool(c < 0) ^ bool(e < 0):
            s(c,e)
        else:
            v(c,e)
    if b == "/\n":
        c = x[1] * x[2]
        e = x[0] * x[3]
        e = int(e)
        f = math.gcd(c,e)
        c = int(c//f)
        e = int(e//f)
        if bool(c < 0) ^ bool(e < 0):
            s(c,e)
        else:
            v(c,e)
                
        