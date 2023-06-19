from sys import stdin
for x in stdin:
    x = list(x)
    if x[0] == "-":
        x.pop(0)
    print(*x,sep="")
