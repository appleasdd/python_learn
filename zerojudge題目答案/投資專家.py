while True:
    try:
        x = int(input())
        for i in range(x):
            y = input()
            y = y.split(" ")
            y = list(map(int,y))
            a = ((y[1] - y[0]) / y[0])*100
            b = a
            if a > 0:         #解決誤差    
                  a += 0.00001

            elif a < 0:
                  a -= 0.00001
            a = round(a,2)
            print("%.2f"%a,"%",sep="",end=" ")
            if b >= 10.00 or b <= -7.00:
                print("dispose")
            else:
                print("keep")
    except:
        break