while True:
    try:
        x = list(input())
        y = int()
        for i in range(len(x)-1):
            if x[i].isalpha() == False and x[i+1].isalpha() != False:
                y += 1
        print(y+1)
    except:
        break