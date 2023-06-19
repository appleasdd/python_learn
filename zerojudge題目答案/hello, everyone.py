while True:
    try:
        x = input()
        x = x.split(" ")
        y = str(input())
        for i in range(len(x)):
            print("{}, {}".format(y,x[i]))
    except:
        break
                
        