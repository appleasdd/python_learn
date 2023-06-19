from sys import stdin
import math
for x in stdin:
    x = int(x)
    a = "{} {}"
    z = int()
    y = stdin.readline()
    y = y.split()
    if y[-1] == "\n":
        y.remove("\n")
    y = list(map(int,y))
    e = list()
    b = set(y)
    b = list(b)
    f = list()
    g = list()
    for i in range(len(b)):
        c = y.count(b[i])
        d = [b[i],c]
        f.append(c)
        e.append(d)
    e.sort( key = lambda e: e[1])
    for i in range(len(e)-1,-1,-1):
        if e[i][1] == max(f):
            g.append([e[i][0],e[i][1]])
        if e[i][1] != max(f):
            break
    for i in range(len(g)-1,-1,-1):
        print(a.format(g[i][0],g[i][1]))

    
        
        