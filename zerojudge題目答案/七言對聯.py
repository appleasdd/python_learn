while True:
    try:
        x = int(input())
        for i in range(x):
            y = input()
            z = input()
            y = y.split()
            z = z.split()
            y = list(map(int,y))
            z = list(map(int,z))
            f = list()
            if (y[1] == y[3] or y[1] != y[5]) or (z[1] == z[3] or z[1] != z[5]):
                f.append("A")
            if y[6] != 1 or z[6] != 0:
                f.append("B")
            if y[1] == z[1] or y[3] == z[3] or y[5] == z[5]:
                f.append("C")
            if len(f) == 0:
                print("None")
            if len(f) != 0:
                for i in range(len(f)):
                    print(f[i],end="")
            f.clear()
            print("\n")

    except:
        break