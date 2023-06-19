from sys import stdin
for x in stdin:
    x = int(x)
    y = int()
    for i in range(x):
        z = stdin.readline()
        z = int(z)
        for j in range(2,z):
            if z % j == 0:
                y += 1
        if y != 0:
            print("N")
        else:
            print("Y")
        y = 0