while True:
    try:
        x = input()
        x = x.split()
        x = list(map(int,x))
        y = list()
        if x[2] < 0:
            while x[0] >= x[1]:
                y.append(x[0])
                x[0] += x[2]
        else:
            while x[0] <= x[1]:
                y.append(x[0])
                x[0] += x[2]
        print(*y)
    except:
        break
                
        