while True:
    try:
            x  = input()
            while x == "":
                x = input()
            x = x.split()
            x = list(map(int,x))
            if len(x) != 1:
                y = int()
                c = len(x) - 1
                x.pop(0)
                for i in range(c):
                    for j in range(0,c-i-1):
                        if x[j] >= x[j+1]:
                            x[j] ,x[j+1] = x[j+1] ,x[j]
                            y += 1
                print(y)
                y = 0    
            else:
                z = input()
                while z == "":
                    z = input()
                z = z.split()
                z = list(map(int,z))
                y = int()
                for i in range(x[0]):
                    for j in range(0,x[0]-i-1):
                        if z[j] >= z[j+1]:
                            z[j] ,z[j+1] = z[j+1] ,z[j]
                            y += 1
                print(y)
                y = 0
    except:
        break
        
    
    
