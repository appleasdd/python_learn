j = 1
y = list()
p = list()
s = list()
while True:
    try:
        for i in range(2):
            x = int(input())
            while j <= x:
                z = x%j
                u = x//j
                if z == 0 and i == 0:
                    y.append(u)
                if z == 0 and i == 1:
                    p.append(u)
                j += 1
            j = 1
            for i in range(len(y)):
                if y[i] in p:
                    s.append(y[i])
        print(max(s))
        
    except:
        break

