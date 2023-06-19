from sys import stdin
for x in stdin:
         x = x.split(" ")
         x = list(map(int,x))
         y = stdin.readline()
         y = y.split(" ")
         y = list(map(int,y))
         a = 0
         b = list()
         for i in range(len(y)):
             a += y[i]
             b.append(a)
         for i in range(x[1]):
             z = stdin.readline()
             z = z.split(" ")
             z = list(map(int,z))
             if z[0] == 1 and z[1] == len(y):
                 print(sum(y))
             elif z[0] != 1 :
                 print(b[z[1]-1]- b[z[0]-2])
             elif z[0] == 1:
                 print(b[z[1]-1])


