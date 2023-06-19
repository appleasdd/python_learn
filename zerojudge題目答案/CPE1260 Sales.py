while True:
    try:
        x = int(input())
        for i in range(x):
            s = int()
            a = -2
            y = int(input())
            z = input()
            z = z.split()
            z = list(map(int,z))
            while y > 0:
                for j in range(a,-(len(z)+1),-1):
                    if z[y-1] >= z[j]:
                        s += 1
                a -= 1
                y -= 1
            print(s)
            a = -2
            s = 0
                
    except:
        break
    
