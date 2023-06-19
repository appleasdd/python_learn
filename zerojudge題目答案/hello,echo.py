while True:
    try:
        x = input()
        y = x.split()
        z = len(y)
        for i in range(z):
            for j in range(len(y)):
                print(y[j],end=" ")
            y.pop(0)
            print("\n")
        
            
    except:
        break
        

