from sys import stdin
import math
for x in stdin:
    x = int(x)
    a = "{} {}"
    z = int()
    y = stdin.readline()
    y = y.split()
    for i in y:
        if '\n' in i:
            y.remove("\n")
    y = list(map(int,y))
    y.sort()
    e = list()
    b = set(y)
    b = list(b)
    f = list()
    for i in range(len(b)):
        c = y.count(b[i])
        d = [b[i],c]
        f.append(c)
        e.append(d)
    e.sort()
    for i in range(len(e)):
        if e[i][1] == max(f):
            print(a.format(e[i][0],e[i][1]))
    
        
        