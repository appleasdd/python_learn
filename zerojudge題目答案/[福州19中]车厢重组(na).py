from sys import stdin
for x in stdin:
    if x != "\n":
        x = int(x)
        z = stdin.readline()
        z = z.split()
        z = list(map(int,z))
        y = int()
        for i in range(x):
            for j in range(0,x-i-1):
                if z[j] >= z[j+1]:
                    z[j] ,z[j+1] = z[j+1] ,z[j]
                    y += 1
        print(y)
        y = 0
        
    
    
