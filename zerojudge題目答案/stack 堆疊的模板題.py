from sys import stdin
for x in stdin:
    if x != "\n":
        x = int(x)
        z = list()
        for i in range(x):
            y = stdin.readline()
            y = y.split()
            y = list(map(int,y))
            if y[0] == 1:
                z.pop(0)
            if y[0] == 2:
                print(z[0])
            if y[0] == 3:
                z.insert(0,y[1])
            
                
        