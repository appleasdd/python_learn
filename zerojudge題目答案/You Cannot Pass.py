while True:
    try:
        x = input()
        x = x.split()
        t = float()
        aver = float()
        x = list(map(int,x))
        for i in range(1,len(x)):
            t += x[i]
        aver = t / (len(x)-1)
        if aver <= 59:
            print("yes")
        elif aver > 59:
            print("no")  
    except :
        break 