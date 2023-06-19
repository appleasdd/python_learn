while True:
    try:
         x = input()
         x = x.split(" ")
         x = list(map(int,x))
         y = input()
         y = y.split(" ")
         y = list(map(int,y))
         a = 0
         for i in range(x[1]):
             z = input()
             z = z.split(" ")
             z = list(map(int,z))
             for j in range(z[0]-1,z[1]):
                 a += y[j]
             print(a)
             a = 0
    except:
        break

