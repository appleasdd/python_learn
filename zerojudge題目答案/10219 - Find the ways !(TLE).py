from sys import stdin
for x in stdin:
    x = x.split()
    x = list(map(int,x))
    a = 1
    y = x[0]
    z = 1
    b = 1
    while a <= x[1]:
        y = y - 1
        b *= y
        z *= a
        a += 1
    c = b // z
    c = str(c)
    c = list(c)
    print(len(c))
