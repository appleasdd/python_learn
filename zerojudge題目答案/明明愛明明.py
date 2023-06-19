while True:
    try:
        x = input()
        x = x.lower()
        x = list(map(str,x))
        x.sort()
        x = ''.join(char for char in x if char.isalnum())
        b = len(x)
        z = int()
        y = list()
        for i in range(len(x)-1):
            if x[i] != x[i+1]:
                y.append(x.count(x[i]))
        y.append(x.count(x[-1]))
        for i in range (len(y)):
            if y[i] % 2 == 1:
                z += 1
        if z <= 1:
            print("yes !")
        else:
            print("no...")
        y.clear()
        z = 0
    except:
        break