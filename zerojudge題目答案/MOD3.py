while True:
    try:
        s = int()
        o = int()
        t = int()
        x = int(input())
        for i in range(x):
            y = int(input())
            z = y % 3
            if z == 0:
                s += 1
            if z == 1:
                o += 1
            if z == 2:
                t += 1
        print(s,o,t)
    
    except:
        break
            
