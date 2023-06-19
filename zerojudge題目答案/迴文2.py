while True:
    try:
        x = list(input())
        y = list(x)
        x.reverse()
        z = int()
        print(x)
        print(y)
        for i in range(len(x)):
            if x[i] == y[i]:
                z += 1
        if z == len(x):
            print("yes")
        else:
            print("no")
    except:
        break
                
        