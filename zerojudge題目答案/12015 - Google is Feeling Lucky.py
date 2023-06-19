while True:
    try:
        x = int(input())
        z = list()
        c = list()
        for i in range(x):
            for j in range(10):
                y = input()
                y = y.split(" ")
                y[1] = int(y[1])
                z.append(y)
                c.append(y[1])
            print("Case #{}:".format(i+1))
            for d in z:
                if max(c) in d:
                    print(d[0])
            z.clear()
            c.clear()      
    except:
        break