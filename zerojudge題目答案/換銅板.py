from sys import stdin
import math
for x in stdin:
    x = int(x)
    y = stdin.readline()
    y = y.split(" ")
    y = list(map(int,y))
    z = int(stdin.readline())
    a = list()
    def fn(f):
        h = len(f)
        if(h == x):
            if (sum([b*c for b,c in zip(f,y)]) == z):
                a.append(f)
            return
        for i in range(z//y[h]+1):
            fn(f + [i])
    fn([])
    a.sort()
    d = "({},{},{})"
    for i in a:
        print("(",end = '')
        print(*i,sep=",",end='')
        print(")")