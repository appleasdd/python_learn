from sys import stdin
for x in stdin:
    x = int(x)
    s = list()
    for i in range(x):
        y = input()
        y = y.split(" ")
        y = list(map(int,y))
        s.append(y)
        s.sort()
    for i in range(len(s)):
        print(*s[i])