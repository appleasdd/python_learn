from sys import stdin
import math
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    i = 1
    z = int()
    y = list()
    gcd = math.gcd(x[0] , x[1])
    a = int(x[0] / gcd)
    b = int(x[1] / gcd)
    while(a % b):
        if (a > b):
            y.append(a//b)
            a %= b
        a , b = b , a
        y.append(0)
    n = math.pow(2,a/b-1);
    while ( len(y) != 0):
        if (y[-1] > 0):
            n *= math.pow(2,y[-1])
        else:
            n += 1
        y.pop(-1)
    print(int(n))
        
        
        
        
    
        
        