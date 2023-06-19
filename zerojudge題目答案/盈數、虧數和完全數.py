from sys import stdin
for x in stdin:
    x = int(x)
    y = int()
    for i in range(1,x):
        if x % i == 0:
          y += i
    if x < y:
        print("盈數")
    elif x > y:
        print("虧數")
    elif x == y:
        print("完全數")
        
    
