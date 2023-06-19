while True:
    try:
        x = int(input())
        a = int()
        b = int()
        c = int()
        d = int()
        e = int()
        for i in range(x):
            y = list(input())
            while y[-1] == " ":
                y.pop(-1)
            y = "".join(y)
            if y == "Get_Kill":
                a += 1
                d += 1
            if y == "Get_Assist":
                b += 1
                continue
            if y == "Die":
                c += 1
                e += 1
            if d < 3 and e == 0:
                print("You have slain an enemie.")
            if d == 3 and e == 0:
                print("KILLING SPREE!")
            if d == 4 and e == 0:
                print("RAMPAGE~")
            if d == 5 and e == 0:
                print("UNSTOPPABLE!")
            if d == 6 and e == 0:
                print("DOMINATING!")
            if d == 7 and e == 0:
                print("GUALIKE!")
            if d >= 8 and e == 0:
                print("LEGENDARY!")
            if d < 3 and e == 1:
                print("You have been slained.")
                e = 0
                d = 0
            if d >= 3 and e == 1:
                print("SHUTDOWN.")
                e = 0
                d = 0
        print("{}/{}/{}".format(a,c,b))
            
    except:
        break
                
        