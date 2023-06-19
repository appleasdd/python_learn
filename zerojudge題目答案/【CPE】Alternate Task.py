k = int()
while True:
    try:
        x = int(input())
        z = list()
        su = int()
        if x == 0:
            break
        if x == 1:
            k += 1
            print("Case {}: {}".format(k,1))
            pass
        for i in range(1,x):
            for j in range(1,x+1):
                if (i % j == 0):
                    su += j
            if su == x:
                z.append(i)
                su = 0
            su = 0
        if len(z) != 0:
            k += 1
            print("Case {}: {}".format(k,max(z)))
        elif len(z) == 0 and x != 1:
            k += 1
            print("Case {}: {}".format(k,-1))
        z.clear()
    except:
        break