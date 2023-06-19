from sys import stdin
for x in stdin:
    x = int(x)
    def a(b,i):
        z = b * (i + 1)
        return z
    y = stdin.readline()
    y = y.split(" ")
    y = list(map(int,y))
    z = int()
    for i in range(x):
        b = y[i]
        z += a(b,i)
    print(z)

    
            
