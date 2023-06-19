while True:
    try:
        x = input()
        x = list(map(int,x))
        for i in range(len(x)):
            print(" ",end = "")
            print(x[i],end = " ")
        print("\n")
        for j in range(len(x)):
            if x[j] == 0:
               print(":.",end=" ")
            if x[j] == 1:
               print(".:",end=" ")
            if x[j] == 2:
               print("..",end=" ")
            if x[j] == 3:
               print(".:",end=" ")
            if x[j] == 4:
               print("..",end=" ")
            if x[j] == 5:
               print(".:",end=" ")
            if x[j] == 6:
               print("..",end=" ")
            if x[j] == 7:
               print(".:",end=" ")
        print("\n")
        for j in range(len(x)):
            if x[j] == 0:
               print("..",end=" ")
            if x[j] == 1:
               print("..",end=" ")
            if x[j] == 2:
               print(".:",end=" ")
            if x[j] == 3:
               print(".:",end=" ")
            if x[j] == 4:
               print(":.",end=" ")
            if x[j] == 5:
               print(":.",end=" ")
            if x[j] == 6:
               print("::",end=" ")
            if x[j] == 7:
               print("::",end=" ")
        print("\n")
        
            
    except:
        break

    