while True:
    try:
        x = input()
        x = x.split(" ")
        x = list(map(int,x))
        x[0] = x[0] + 2
        x[1] = x[1] + 30
        if x[1] >= 60:
            x[0] += 1
            x[1] = abs(60 - x[1])
        if x[0] > 23:
            x[0] = x[0] - 24
        if x[0] // 10 == 0:
            print("0",x[0],":",sep="",end="")
        else:
            print(x[0],":",sep="",end="")
        if x[1] // 10 == 0:
            print("0",x[1],sep="",end="")
        else:
            print(x[1],sep="")
    except:
        break

                
        
    
            
