while True:
    try:
        x = list(input())
        y = len(x)
        for i in range(y):
            print(*x,sep="")
            x.append(x[0])
            x.pop(0)
    except:
        break

                
        
    
            
