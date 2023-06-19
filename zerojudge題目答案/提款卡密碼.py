while True:
    try:
        x ={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9
        ,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19
        ,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}
        y = list(input())
        c = list()
        for i in range(len(y)-1):
            z1 = x.get(y[i])
            z2 = x.get(y[i+1])
            if z2 < z1:
                z3 = z2
                z2 = z1
                z1 = z3
            z3 = z2 - z1
            c.append(z3)
        for i in range(len(c)):
            print(c[i],end="")
        print("\n")
    except:
        break
