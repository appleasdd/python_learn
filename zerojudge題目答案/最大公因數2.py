j = 1
y = list()
p = list()
s = list()
while True:
    try:
        x = input()
        x = x.split(' ')
        x = list(map(int,x))
        for i in range(len(x)):
            while j <= x[i]:
                z = x[i]%j
                u = x[i]//j
                if z == 0 and i == 0:
                    y.append(u)
                if z == 0 and i == 1:
                    p.append(u)
                j += 1
            j = 1
            for i in range(len(y)):
                if y[i] in p:
                    s.append(y[i])
        print(y)
        print(p)
        print(max(s))
    except:
        break

