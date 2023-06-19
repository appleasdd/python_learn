while True:
    try:
        x = list(input())
        y = len(x)
        for i in range(len(x)):
            for j in range(len(x)):
                print((x[j]),end=" ")
            print("\n")
            x.pop(-1)
    except:
        break

