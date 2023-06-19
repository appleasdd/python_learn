from sys import stdin
for x in stdin:
    if x != "\n":
        x = x.split()
        x = list(map(int,x))
        z = stdin.readline()
        z = z.split()
        z = list(map(int,z))
        y = int()
        if len(x) != 1:
            c = x[0]
            x.pop(0)
            for i in range(len(x)):
                for j in range(0,len(x)-i-1):
                    if x[j] > x[j+1]:
                        x[j] ,x[j+1] = x[j+1] ,x[j]
                        y += 1
            print(y)
        else:
            for i in range(len(z)):
                for j in range(0,len(z)-i-1):
                    if z[j] > z[j+1]:
                        z[j] ,z[j+1] = z[j+1] ,z[j]
                        y += 1
            print(y)
        
    
    
