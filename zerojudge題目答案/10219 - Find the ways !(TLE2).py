from sys import stdin
from math import factorial
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    a = 1
    y = x[0]
    e = x[0]-x[1]
    b = factorial(x[0])
    d = factorial(e)
    z = factorial(x[1])
    c = (b // d) // z
    c = str(c)
    c = list(c)
    print(len(c))
