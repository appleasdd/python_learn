y = list()
while True:
    try:
        x = list(input())
        for i in range(len(x)):
            if i == (len(x)/2):
                break
            if x[i] == x[-(i+1)]:
                y.append(1)
            else:
                if x[i] != x[-(i+1)]:
                    y.append(0)
        for i in range(len(y)):
            if y[i] == 0:
                print('no')
                break
            if (i+1) == (len(y)):
                print('yes')
        y.clear()
    except EOFError:
        break

