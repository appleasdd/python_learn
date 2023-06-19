while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))
        y = []
        for i in range(x[0]):
            z = input()
            z = z.split(" ")
            z = list(map(int,z))
            y.append(z)
        for i in range(x[1]):
            for j in range(x[0]):
                print(y[j][i], end=" ")
            print("\n")
    except:
        break

