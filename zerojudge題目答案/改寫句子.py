while True:
    try:
        x = list(input())
        for i in range(len(x)):
            if x[i] == "@":
                print(x[i],"【跳1行】",sep="")
                print(1,end="")
                continue
            if x[i] == "$":
                print(x[i],"【跳2行】",sep="")
                print(1)
                print(2,end="")
                continue
            if x[i] == "#":
                print(x[i],"【跳3行】",sep="")
                print(1)
                print(2)
                print(3,end="")
                continue
            if x[i] == "!":
                print(x[i],"【跳4行】",sep="")
                print(1)
                print(2)
                print(3)
                print(4,end="")
                continue
            if x[i] == "%":
                print(x[i],"【跳5行】",sep="")
                print(1)
                print(2)
                print(3)
                print(4)
                print(5,end="")
                continue
            print(x[i],end="",sep="")
    except:
        break

    