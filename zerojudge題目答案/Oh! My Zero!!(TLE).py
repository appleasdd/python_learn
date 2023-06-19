from sys import stdin
for x in stdin:
    x = int(x)
    j = 1
    for i in range(1,x+1):
        j *= i
    j = str(j)
    i = j.count("0")
    print(i)
    
    
                
        