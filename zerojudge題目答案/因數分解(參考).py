from sys import stdin
def gp(n,k):#檢測i及二是否為n的質因數及求n可以連除幾次k
    c = 0
    while(n % k == 0):
        c += 1
        n //= k
    return n ,c
def fmt(x,y):
    if(y==1):
        return str(x)
    return "{}^{}".format(x,y)
for x in stdin:
    n = int(x)
    m = int(n**0.5)+1
    r = []
    n , c = gp(n, 2)#判斷2是否為n的質因數
    if(c > 0):
        r.append(fmt(2,c))
    for i in range(3,m,2):
        if (i > n):
            break
        n,c = gp(n,i)#可以測出i是否為n的質因數
        if(c>0):
            r.append(fmt(i,c))
    if(n>1):
        r.append(fmt(n,1))
    print(' * '.join(r))
        

