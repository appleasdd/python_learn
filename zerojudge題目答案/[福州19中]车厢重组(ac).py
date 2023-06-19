while True:
    try:
        x = input()
        y = list()
        w = int()
        while x == "":
            x = input()
        x = x.split()
        x = list(map(int,x))
        y.extend(x)
        while len(y) <= y[0]:
            x = input()
            while x == "":
                x = input()
            x = x.split()
            x = list(map(int,x))
            y.extend(x)
        c = len(y) - 1
        y.pop(0)
        for i in range(c):
            for j in range(0,c-i-1):
                if y[j] > y[j+1]:
                    y[j] , y[j+1] = y[j+1] , y[j]
                    w += 1
        print(w)
    except:
        break
        
    
    
