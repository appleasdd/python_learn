x = {"A" : 1,"B" : 10,"C" : 19,
     "D" : 28,"E" : 37,"F" : 46,
     "G" : 55,"H" : 64,"I" : 39,
     "J" : 73,"K" : 82,"L" : 2,
     "M" : 11,"N" : 20,"O" : 48,
     "P" : 29,"Q" : 38,"R" : 47,
     "S" : 56,"T" : 65,"U" : 74,
     "V" : 83,"W" : 21,"X" : 3,
     "Y" : 12,"Z" : 30}
i = int()
while True:
    try:
        a = input()
        y = list(a)
        y[0] = x.get(y[0])
        y = list(map(int,y))
        e = (y[0] + y[1]*8 + y[2]*7 + y[3]*6 + y[4]*5 + y[5]*4 + y[6]*3 + y[7]*2 + y[8]*1 + y[9])% 10
        if e == 0:
            print("real")
        else:
            print("fake")
    except:
        break
