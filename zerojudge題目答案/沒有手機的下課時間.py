from sys import stdin
for x in stdin:
    x = list(x)
    x.pop(-1)
    x = list(map(int,x))
    y = stdin.readline()
    y = int(y)
    a = int()
    b = int()
    for i in range(y):
        z = stdin.readline()
        z = list(z)
        z.pop(-1)
        z = list(map(int,z))
        for j in range(len(x)):
            for k in range(len(z)):
                if x[j] == z[k] and j == k:
                    a += 1
                elif x[j] == z[k] and j != k:
                    b += 1
        print("{}A{}B".format(a,b))
        a = 0
        b = 0
                    
