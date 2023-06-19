from sys import stdin
for x in stdin:
    x = int(x)
    def a(x):
        y.append(y[3] * x)
    def b(x):
        y.append(y[3] + x)
    for i in range(x):
        y = stdin.readline()
        y = y.split()
        y = list(map(int,y))
        if y[3] - y[2] != y[1] - y[0]:
            a(y[3] // y[2])
        else:
            b(y[3] - y[2])
        print(*y)
        
    
