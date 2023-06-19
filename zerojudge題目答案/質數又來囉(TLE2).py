while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))
        x.sort()
        i = 2
        z = int()
        while x[0] <= x[1]:
            while i < x[0]:
                if x[0] % i == 0 or x[0] % 2 == 0:
                    break
                i += 1
            if i == x[0]:
                z += 1
            i = 2
            x[0] += 1
        print(z)
    except :
        break