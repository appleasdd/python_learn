while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))
        r = float()
        t = float()
        q = (x[0]*x[4]) - (x[1]*x[3]) 
        w = (x[2]*x[4]) - (x[1]*x[5])
        e = (x[0]*x[5]) - (x[3]*x[2])
        if q != 0 and (w != 0 or e != 0):
            r = w / q
            t = e / q
            print("x=%.2f"%r)
            print("y=%.2f"%t)
        if q == 0 and (w != 0 or e != 0):
            print("No answer")
        if q == 0 and w == 0 and e == 0:
            print("Too many")
            
    except:
        break
    
    