while True:
    try:
        x = int(input())
        z = int()
        for i in range(x):
            y = list(input())
            y = list(map(int,y))
            z = y[0]
            for i in range(1,len(y)):
                z *= y[i]
            print(z)
            
    except :
        break