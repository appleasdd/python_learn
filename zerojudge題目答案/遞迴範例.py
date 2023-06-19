from sys import stdin
for x in stdin:
    def a(x):#降冪
        if x > 0:
            return(a(x-1) * x)
        else:
            return(1)
    def b(y,x):#升冪
        if y <= x:
            return(b(y+1,x) * y)
        else:
            return (1)
    x = int(x)
    print(a(x))
    print(b(1,x))