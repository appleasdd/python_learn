b = int()
c = int()
e = int()
x = 0
d = []
f = []
j = 2
a = int(input())
for i in range (a):
    b = a // (i + 1)
    c = a % (i + 1)
    if c == 0:
        d.append(b)
print(d)
for i in range (len(d)):
        while j < d[i]:
            e = (d[i]) % (j)
            j = j + 1
            if e == 0:
                f.append(d[i])
                break;
        j = 2
for i in range(len(f)):
     d.remove(f[i])
d.remove(1)
d.reverse()
c = 0
for i in range(len(d)):
    while (a % d[i]) == 0:
        x = x + 1
        b = a / d[i]
        a = b
    if x <= 1:
        print(d[i],end='')
    else:
        print(d[i],"^",x,end='',sep='')
    if (a != 1):
            print(" * ",end='')
    x = 0