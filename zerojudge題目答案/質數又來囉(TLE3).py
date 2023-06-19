from sys import stdin
import math
for x in stdin:
  x = x.split() 
  x = list(map(int,x))
  v = int()
  for i in range(x[0],x[1]+1):
    a = math.floor(i**0.5)
    if a == 1 and i != 1:
        v += 1
    for j in range(2,a+1):
        if i % j == 0:
            break
        if j == a:
            v += 1
  print(v)
    
    
