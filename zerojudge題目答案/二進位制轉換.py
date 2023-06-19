z = list()
i = int()
while True:
    try:
        x = int(input())
        while x >= 1:
            i = x % 2
            x = x // 2
            z.append(i)
        z.reverse()
        for j in range(len(z)):
            print(z[j],sep = "",end = "")
        print("\n")
        z.clear()
            
    except:
        break


