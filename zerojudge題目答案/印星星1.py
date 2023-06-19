while True:
    try:
        x = int(input())
        for i in range(1,x+1):
            print("*",sep="",end="")
        print("\n")
        for i in range(1,x+1):
            print("*")
        print("\n")
        for i in range(1,x+1):
            print(i*"*")
        print("\n")
        for i in range(1,x+1):
            print("{:>{}}".format(i*"*",x))
        print("\n")
        for i in range(x,0,-1):
            print("{:>{}}".format(i*"*",x))
        print("\n")
        for i in range(x,0,-1):
            print("{:<{}}".format(i*"*",x))
        print("\n")
        for i in range(1,x+1):
            if i%2 != 0:
                print("{:^{}}".format(i*"*",x))
        print("\n")
        for i in range(x,0,-1):
            if i%2 != 0:
                print("{:^{}}".format(i*"*",x))
        print("\n")
        a = x // 2
        z = a+1
        for i in range(1,x+2):
            if (i <= a):
                print("{:<{}}".format(i*"*",x))
            if (i > a):
                print("{:<{}}".format(z*"*",x))
                z -= 1
        print("\n")
        a = x // 2
        z = a+1
        for i in range(1,x+2):
            if (i <= a):
                print("{:>{}}".format(i*"*",x))
            if (i > a):
                print("{:>{}}".format(z*"*",x))
                z -= 1
        print("\n")
        for i in range(1,(x*2)+1):
            if i%2 != 0:
                print("{:^{}}".format(i*"*",x*2+1))
        print("\n")
        for i in range((x*2),0,-1):
            if i%2 != 0:
                print("{:^{}}".format(i*"*",x*2+1))
        print("\n")
        a = (x*2 // 2)-1
        z = a+1
        for i in range(1,(x*2)+2):
            if (i <= a):
                print("{:<{}}".format(i*"*",x))
            if (i > a):
                print("{:<{}}".format(z*"*",x))
                z -= 1
        print("\n")
        a = (x*2 // 2)-1
        z = a+1
        for i in range(1,(x*2)+2):
            if (i <= a):
                print("{:>{}}".format(i*"*",x))
            if (i > a):
                print("{:>{}}".format(z*"*",x))
                z -= 1
        print("\n")
        for i in range(1,x+1):
            if (x % 2 !=0):
                if (i %2 == 1):
                    print(""," ".join("{:^{}}".format(i*"*",x+1)))
                if (i %2 == 0):
                    print(" ".join("{:^{}}".format(i*"*",x+1)))
            if (x % 2 ==0):
                if (i %2 == 1):
                    print(" ".join("{:^{}}".format(i*"*",x+1)))
                if (i %2 == 0):
                    print(""," ".join("{:^{}}".format(i*"*",x+1)))
        print("\n")
        for i in range(x,0,-1):
            if (x % 2 !=0):
                if (i %2 == 1):
                    print(""," ".join("{:^{}}".format(i*"*",x+1)))
                if (i %2 == 0):
                    print(" ".join("{:^{}}".format(i*"*",x+1)))
            if (x % 2 ==0):
                if (i %2 == 1):
                    print(" ".join("{:^{}}".format(i*"*",x+1)))
                if (i %2 == 0):
                    print(""," ".join("{:^{}}".format(i*"*",x+1)))
    except:
        break
    
    