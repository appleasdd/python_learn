while True:
    try:
        a = int()
        a2= int()
        p = int(1)
        d = list()
        x = int(input())
        for i in range(x):
            o = int(input())
            t = int(input())
            while p <= t:
                
                a = p**2
                if a <= t and a >= o:
                    a2 += a
                p += 1
            d.append(a2)
            b = "Case {}:"
            print(b.format(i+1),d[i])
            p = 0
            a2 = 0
    except:
        break
            
