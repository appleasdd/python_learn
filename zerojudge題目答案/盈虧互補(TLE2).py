from sys import stdin
for x in stdin:
    x = int(x)
    if x == 0:
        break
    y = 0
    z = 0
    for i in range(1,(x//2)+1):
        if x % i == 0:
            y += i
    if x == y:
        print("=",x,sep="")
    elif x != y:
        for i in range(1,(y//2)+1):
            if y % i == 0:
                z += i
        if x == z:
            print(y)
        else:
            print(0)
        
    
