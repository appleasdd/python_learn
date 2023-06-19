from sys import stdin
import math
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    i = 1
    def f(n):
        if n == 1:
            return 1
        if n % 2 == 0:
            return 1 + f(n/2)
        if n % 2 != 0:
            return 1 / f(n-1)
    y = x[0] / x[1]
    y = math.floor (y * 10**3) / (10**3)
    while math.floor (f(i) * 10**3) / (10**3) != y:
        i += 1
    print(i)
        
        
        
    
        
        