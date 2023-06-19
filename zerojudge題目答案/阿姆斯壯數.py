while True:
    try:
        a = int()
        i = int()
        x = input()
        k = list()
        x = x.split()
        x = list(map(int,x))
        z = len(list(str(x[1])))
        if x[0] > x[1]:
            y = x[0]
            x[0] = x[1]
            x[1] = y
        while x[0] <= (x[1]):
            p = list(map(int,list(str(x[0]))))
            for i in range(len(p)):
                a += p[i]**len(p)
            if x[0] == a:
                k.append(x[0])
            a = 0
            x[0] += 1
        if len(k) == 0:
            print("none")
            break
        for i in range(len(k)):
            print(k[i],end=" ")     
    except:
        break
        

 