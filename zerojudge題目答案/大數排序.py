while True:
    try:
        x = int(input())
        y = list()
        for i in range(x):
            z = int(input())
            y.append(z)
            y.sort()
        for i in range(len(y)):
            print(y[i])
    except:
        break