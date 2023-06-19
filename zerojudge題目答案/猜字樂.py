while True:
    try:
        x = list(input())
        i = 1
        print(x)
        for i in range(len(x)):
            print(x[i],end="",sep=" ")
            if x[i] == "@":
                print("【跳1行】")
                while i < 1:
                    print(i)
                    i += 1
                print(1,end="")
            if x[i] == "$":
                print("【跳2行】")
                while i < 2:
                    print(i)
                    i += 1
                print(2,end="")
            if x[i] == "#":
                print("【跳3行】")
                while i < 3:
                    print(i)
                    i += 1
                print(3,end="")
            if x[i] == "!":
                print("【跳4行】")
                while i < 4:
                    print(i)
                    i += 1
                print(4,end="")
            if x[i] == "%":
                print("【跳5行】")
                while i < 5:
                    print(i)
                    i += 1
                print(5,end="")
                    
    except:
        break
