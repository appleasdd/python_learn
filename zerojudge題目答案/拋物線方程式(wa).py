from sys import stdin
import math
for d in stdin:
    def gcd2(a,b):
        if b == 0:
            return a
        else:
            return gcd2(b, a % b)
    def gcd4(r,a,b,c):
        return gcd2(gcd2(r,a),gcd2(b,c))
    d = d.split(" ")
    d = list(map(int,d))
    a = int()
    b = int()
    c = int()
    h,k,x,y = d[0],d[1],d[2],d[3]
    a = (y-k)/(x-h)**2
    c = a * (h**2) + k
    b = -(2 * h * (y - k))
    r = abs(x-h)
    a = a * r
    c = a * (h**2) + (k * r)
    a,b,c,r = int(a),int(b),int(c),int(r)
    a = a // gcd4(a,b,c,r)
    b = b // gcd4(a,b,c,r)
    c = c // gcd4(a,b,c,r)
    r = r // gcd4(a,b,c,r)
    e = "{}y = {}x^2 + {}x + {}"
    print(e.format(r,a,b,c))
    