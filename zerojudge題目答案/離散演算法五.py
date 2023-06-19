y = input()
y = y.split()
y = list(map(int,y))
z = list()
x = 1
power = y[0] % y[2]
while y[1] >= 1:
            i = y[1] % 2
            y[1] = y[1] // 2
            z.append(i)
z.reverse()
print(*z)
for i in range(len(z)-1,-1,-1):
    if z[i] == 1:
        x = (x * power) % y[2]
    power = (power**2) % y[2]
    print(x,power)
    
