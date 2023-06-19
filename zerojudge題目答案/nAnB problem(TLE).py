from sys import stdin
for x in stdin:
        if x != "\n":
            x = x.split(" ")
            x = list(map(int,x))
            y = int(input())
            p = 0
            q = 0
            c = list()
            b = list()
            for i in range(y):
                z = input()
                z = z.split(" ")
                z = list(map(int,z))
                for j in range(len(x)):
                    b.append(x[j])
                    if z[j] == b[j]:
                        z[j] = 0
                        b[j] = 0
                        p += 1
                for a in b:
                    if a in z and a != 0:
                        q += 1
                print(p,"A",q,"B",sep="")
                p = 0
                q = 0
                b.clear()
