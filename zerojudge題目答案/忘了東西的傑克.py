from sys import stdin
import math
for x in stdin:
    x = int(x)
    z = int()
    for i in range(x):
        y = stdin.readline()
        y = y.split(" ")
        y = list(map(int,y))
        z = y[0] * 60 + y[1] + y[4]
        z2 = y[2] * 60 + y[3]
        if z <= z2:
            print("Yes")
        elif z > z2:
            print("No")
        
        
        
        
    
        
        