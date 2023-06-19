import sys
x = {"A" : 1,"B" : 10,"C" : 19,
     "D" : 28,"E" : 37,"F" : 46,
     "G" : 55,"H" : 64,"I" : 39,
     "J" : 73,"K" : 82,"L" : 2,
     "M" : 11,"N" : 20,"O" : 48,
     "P" : 29,"Q" : 38,"R" : 47,
     "S" : 56,"T" : 65,"U" : 74,
     "V" : 83,"W" : 21,"X" : 3,
     "Y" : 12,"Z" : 30}
z = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i = int()
e = int()
while True:
    try:
        a = input()
        y = list(a)
        p = list()
        if len(y) == 9:
            y = list(map(int,y))
            e = (10-(y[0] + y[1]*8 + y[2]*7 + y[3]*6 + y[4]*5 + y[5]*4 + y[6]*3 + y[7]*2 + y[8]*1)%10)
            for i in range(len(x)):
                s = x.get(z[i])
                y.insert(0,s)
                y = list(map(int,y))
                c = (10-(y[0] + y[1]*8 + y[2]*7 + y[3]*6 + y[4]*5 + y[5]*4 + y[6]*3 + y[7]*2 + y[8]*1 + y[9])%10)
                if c == 10:
                    p.append(z[i])
                y.pop(0)
        for i in range(len(p)):
            print(p[i],end="",sep="")
    except:
        break
