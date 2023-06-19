from sys import stdin
for x in stdin:
    x = int(x)
    j = 0
    while x >= 5:
        j += x // 5
        x //= 5
    j = int(j)
    print(j)
    
    
                
        