while True:
    try:
        y = input()
        y = y.split(" ")
        y = list(map(eval,y))
        print("%.{}f".format(y[2])%(y[0]/y[1]))
    except:
        break