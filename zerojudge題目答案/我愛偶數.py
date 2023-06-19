from sys import stdin
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    y = int()
    y = ((x[1]-x[1]%2)-(x[0]+x[0]%2))//2+1
    print(y)
        