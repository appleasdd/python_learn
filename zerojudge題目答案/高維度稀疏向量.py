from sys import stdin
for x in stdin:
    x = x.split(" ")
    a = stdin.readline()
    a = a.split(" ")
    d = int()
    c = int()
    for i in range(len(x)):
        x[i] = x[i].split(":")
        x[i] = list(map(int,x[i]))
    for j in range(len(a)):
        a[j] = a[j].split(":")
        a[j] = list(map(int,a[j]))
        for i in range(len(x)):
            if a[j][0] == x[i][0]:
                c += a[j][1] * x[i][1]
    print(c)
        