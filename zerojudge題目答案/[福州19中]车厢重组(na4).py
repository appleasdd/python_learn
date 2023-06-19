while True:
    try:
        x = input()
        y = list()
        while x == "":
            x = input()
        x = int(x)
        w = int()
        for i in range(x):
            z = input()
            while z == "":
                z = input()
            z = int(z)
            y.append(z)
        for i in range(x):
            for j in range(0,x-i-1):
                if y[j] > y[j+1]:
                    y[j] , y[j+1] = y[j+1] , y[j]
                    w += 1
        print(w)
    except:
        break
    
    
