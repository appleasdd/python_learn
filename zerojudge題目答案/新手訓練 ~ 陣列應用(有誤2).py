while True:
    try:
        y = input()
        y = y.split(" ")
        y = list(map(int,y))
        z = float(y[0] / y[1])
        b = ("%.{}f".format(y[2]+1)%(z))
        a = list(b)
        for i in range(len(a)-1):
            print(a[i],end="")
        print("\n")
        
    except:
        break