y = list()
while True:
    try:
        x = list(input())
        x = list(map(int,x))
        x.reverse()
        for i in range (len(x)):
            if x[i] == 0:
                y.append(x[i])
        if x == y and len(x) != 1:
            print(0)
        if len(x) != 1:
            while x[0] == 0:
                x.remove(0) 
        for i in range (len(x)):    
            print(x[i],end='')
    except:
        break

