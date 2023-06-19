y = int()
while True:
    try:
        x = input()
        x = x.split(' ')
        x = list(map(int,x))
        if x[0] < x[1]:
            x.reverse()
        while x[0] or x[1] == 0:
            y = x[0] % x[1]
            x[0] = x[1]
            x[1] = y
        print(max(x))
    except:
        break


