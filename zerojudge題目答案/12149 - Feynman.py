while True:
    try:
        x = int(input())
        if x == 0:
            break
        if x == 1:
            print(1)
        if x != 1:
            print(x*(x+1)*(2*x+1)//6)
    except:
        break