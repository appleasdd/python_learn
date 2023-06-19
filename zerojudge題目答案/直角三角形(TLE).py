from sys import stdin
from itertools import combinations
for x in stdin:
    x = int(x)
    for i in range(x):
        y = int(stdin.readline())
        z = stdin.readline()
        z = z.split(" ")
        z = list(map(int,z))
        a = list(combinations(z,3))
        c = set(a)
        c = list(map(list,c))
        a = list(map(list,a))
        b = int()
        for e in range(len(c)):
            c[e].append(a.count(c[e]))
        for j in range(len(c)):
            if (c[j][0]**2) + (c[j][1]**2) == (c[j][2]**2):
                b += c[j][3]
        print(b)
        c.clear()
        a.clear()
        b = 0
                
        