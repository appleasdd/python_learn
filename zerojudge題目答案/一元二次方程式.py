import math
while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))#x[0] = a ,x[1] = b , x[2] = c
        d = x[1]**2 - 4*x[0]*x[2]
        x3 = int()
        if d > 0:
            x1 = ((-x[1]) + (x[1]**2 - 4*x[0]*x[2])**0.5)/(2*x[0])
            x2 = ((-x[1]) - (x[1]**2 - 4*x[0]*x[2])**0.5)/(2*x[0])
            x1 = int(x1)
            x2 = int(x2)
            if x1 <= x2:
                print("Two different roots x1={} , x2={}".format(x2,x1))
            elif x1 > x2:
                print("Two different roots x1={} , x2={}".format(x1,x2))
        elif d == 0:
            x3 = -x[1] / (2 * x[0])
            print('Two same roots x=%d' % x3)
        elif d < 0:
            print("No real root")

    except:
        break

    