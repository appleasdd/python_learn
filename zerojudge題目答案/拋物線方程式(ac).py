from sys import stdin
import math
for d in stdin:
    d = d.split(" ")
    d = list(map(int,d))
    a = int()
    b = int()
    c = int()
    h,k,x,y = d[0],d[1],d[2],d[3]
    a = (x - h)**2
    b = (y-k)
    c = -2*h*(y-k)
    r = (y-k)*(h**2) + k*((x-h)**2)
    a,b,c,r = int(a),int(b),int(c),int(r)
    gcd2 = math.gcd(math.gcd(a,b),math.gcd(c,r))
    a = a // gcd2 
    b = b // gcd2
    c = c // gcd2
    r = r // gcd2
    e = "{}y = {}x^2 + {}x + {}"
    print(e.format(a,b,c,r))
    