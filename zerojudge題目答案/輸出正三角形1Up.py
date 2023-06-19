while True:
    try:
        x = int(input())
        for i in range(1,(x*2)+1):
            if i % 2 != 0:
                print("{:^{}}".format(i*"*",(x*2)+1))
    except:
        break
    
    
    