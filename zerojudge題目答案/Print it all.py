while True:
    try:
        x = 1
        while x != 0:
            x = int(input())
            if x == 0:
                break
            for i in range(1,x):
                if i % 7 != 0:
                    print(i,end = " ")
            print("\n")
    except :
        break 