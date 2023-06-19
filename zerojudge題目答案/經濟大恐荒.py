from sys import stdin
for x in stdin:
    x = int(x)
    z = int()
    y = stdin.readline()
    y = y.split()
    y = list(map(int,y))
    for i in range(1,x+1):
        z += i * y[i-1]
    print(z)
    
    
