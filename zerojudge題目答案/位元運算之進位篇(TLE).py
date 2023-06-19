import sys
while True:
    try:
        x = int(sys.stdin.readline())
        y = list(bin(x))
        y.pop(0)
        y.pop(0)
        y = list(map(int,y))
        z = 0
        if x != 0:
            for i in range((len(y)-1),-1,-1):
                y[i] += 1
                if y[i] > 1:
                    z += 1
                if y[i] <= 1:
                    break
            print(z)
        else:
            break
    except:
        break

