from itertools import permutations
while True:
    try:
        x = int(input())
        y = list()
        for i in range(1,x+1):
            y.append(i)
        z = list(permutations(y,len(y)))#做排列
        z.reverse()
        for i in range(len(z)):
            z[i] = list(map(str,z[i]))#將z[i]中的所有元素轉成str
            print("".join(z[i]))#消除框框(int不可以用join)
    except:
        break