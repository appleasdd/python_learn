while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))
        j = int(2)
        z = int()
        y = int()
        s = int()
        for i in range(x[0],x[1]+1):
            while j < i:
                y = i % j
                if y == 0:
                    z += 1
                    break
                j += 1
            j = 2
        s = (x[1]+1-x[0]) - z
        print(s)   
    except :
        break 