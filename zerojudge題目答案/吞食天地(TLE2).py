from sys import stdin
for x in stdin:
         x = x.split(" ")
         x = list(map(int,x))
         y = stdin.readline()
         y = y.split(" ")
         y = list(map(int,y))
         a = 0
         for i in range(x[1]):
             z = stdin.readline()
             z = z.split(" ")
             z = list(map(int,z))
             if z[0] == 1 and z[1] == len(y):
                 print(sum(y))
             else:
                 for j in range(z[0]-1,z[1]):
                     a += y[j]
                 print(a)
                 a = 0


