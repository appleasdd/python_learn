while True:
    try:
        x = int(input())
        for i in range(x):
            y = input()
            y = y.split(" ")
            y = list(map(eval,y))
            if y[0] == 1:
                print(y[1] + y[2])
            if y[0] == 2:
                print(y[1] - y[2])
            if y[0] == 3:
                print(y[1] * y[2])
            if y[0] == 4:
                print(y[1] // y[2])
            y.clear()
    except:
        break