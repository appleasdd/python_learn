from sys import stdin
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    z = list()
    for i in range(x[0]):
        y = stdin.readline()
        y = y.split()
        y = list(map(int,y))
        z.append(y)
    for i in range(x[1]):
        for j in range(x[0]):
            print(z[j][i],end=" ")
        print("\n")
    
