while True:
    try:
        x =input()
        x = x.split(" ")
        x = list(map(int,x))
        if x[0] > x[1]:
            print(x[1]+1)
        if x[0] == x[1]:
            print(x[1])
        
    except:
        break