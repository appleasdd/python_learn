from sys import stdin
import math
for x in stdin:
    x = int(x)
    y = 0
    z = math.floor(x**0.5)
    z = int(z)
    for i in range(2,z+1):
        if x % i == 0:
            y += 1
    if y == 0:
        print("質數")
    if y != 0:
        print("非質數")