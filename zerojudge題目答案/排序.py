while True:
    try:
        x = int(input())
        z = input()
        y = z.split(" ")
        print(y)
        y = list(map(int,y))
        y.sort()
        for i in range(x):
            print(y[i],end=" ")
        print("\n")
    except :
        break 