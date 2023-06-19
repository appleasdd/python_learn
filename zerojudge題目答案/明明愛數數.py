while True:
    try:
        x = input()
        x = x.split()
        x = list(map(int,x))
        i = x[0]
        z = 1
        y = x[0]
        while y <= x[1]:
            y += (i+1)
            i += 1
            z += 1
        print(z)
    except :
        break 