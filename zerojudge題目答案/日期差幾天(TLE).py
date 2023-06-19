w1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
w2 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
while True:
    try:
        x = input()
        x = x.split()
        x = list(map(int,x))
        y = input()
        y = y.split()
        t = list()
        y = list(map(int,y))
        z = int()
        if x[1] < y[1]:
            t = x
            x = y
            y = t
        if x[0] == y[0]:
            b = x[0]%4
            c = x[0]%100
            d = x[0]%400
            if b == 0 and c != 0 or d == 0:
                if x[1] == y[1]:
                    if x[2] < y[2]:
                        t = x[2]
                        x[2] = y[2]
                        y[2] = t 
                    z+=(x[2]-y[2])
                else:
                    z += (w2.get(y[1])-y[2])
                    z += x[2]
                    for i in range(y[1]+1,x[1]):
                        z += w2.get(i)
            else:
                    if x[1] == y[1]:
                        if x[2] < y[2]:
                            t = x[2]
                            x[2] = y[2]
                            y[2] = t 
                        z+=(x[2]-y[2])
                    else:
                        z += (w1.get(y[1])-y[2])
                        z += x[2]
                        for i in range(y[1]+1,x[1]):
                            z += w1.get(i)
        if x[0] < y[0]:
            t = x
            x = y
            y = t
        for i in range(y[0],x[0]):
                b = i%4
                c = i%100
                d = i%400
                if b == 0 and c != 0 or d == 0:
                    z+=366
                else:
                    z+=365
        print(z)
        
          
        
    except:
        break