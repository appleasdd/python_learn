while True:
    try:
        x = int(input())
        z = list()
        w = int()
        for i in range(x):
            y = input()
            y = y.split()
            y = list(map(int,y))
            for j in range(y[0]):
                  p = input()
                  p = p.split()
                  p = list(map(int,p))
                  z.extend(p)
            c = z.copy()
            c.reverse()
            for i in range(1,len(z)+1):
                if z[i-1] == c[i-1]:
                    w += 1
            if w == len(z):
                print("go forward")
            elif w != len(z):
                print("keep defending")
            w = 0
            z.clear()
            c.clear()
    except:
        break
        
    
    
