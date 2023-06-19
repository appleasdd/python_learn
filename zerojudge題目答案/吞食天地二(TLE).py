from sys import stdin
for x in stdin:
    x = x.split(" ")
    x = list(map(int,x))
    z = list()
    a = 0
    for i in range(x[0]):
        y = stdin.readline()
        y = y.split()
        y = list(map(int,y))
        z.append(y)
    for i in range(x[1]):
        q = stdin.readline()
        q = q.split()
        q = list(map(int,q))
        if q[0] == q[2]:
            for j in range(q[1]-1,q[3]):
               a += z[q[0]-1][j]
            print(a)
            a = 0
        if q[1] == q[3]:
            for j in range(q[0]-1,q[2]):
                a += z[j][q[0]-1]
            print(a)
            a = 0
        if q[0] != q[2] and q[1] != q[3]:
            for j in range(q[1]-1,q[3]):
                for b in range(q[0]-1,q[2]):
                    a += z[j][b]
            print(a)
            a = 0