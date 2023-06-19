x = int(input())
i = 0
a = x
"""
(一列)
while i <= x:
    print("*",end="")
    i += 1
"""
"""
(一行)
while i < x:
    print("*")
    i += 1
"""
"""
(對左)
while i <= x:
    print("%s"%(i*"*"))
    i += 1"""
"""
(靠左下)
while x >= i:
    print("%s"%(x*"*"))
    x -= 1
"""
"""
(靠右)
while i <= x:
    print("%s"%(a*" "),"%s"%(i*"*"))
    i += 1
    a -= 1
"""
"""
(靠右下)
a = 0
while x >= i:
    print("%s"%(a*" "),"%s"%(x*"*"))
    x -= 1
    a += 1
"""
"""
(中間金字塔單數)
while i <= x:
    if i % 2 == 1:
        print('{:^{}}'.format(i*"*",x))
    i += 1
"""
"""
(倒立金字塔單數)
b = x
while x >= i:
    if x % 2 == 1:
        print('{:^{}}'.format(x*"*",b))
    x -= 1
"""
"""
(左側金字塔單數)
b = x*2
while i <= x*2-1:
    if i <= x:
        print("%s"%(i*"*"))
        i += 1
    if i <= x*2 and i > x:
        print("%s"%((b-i)*"*"))
        i += 1
"""
"""
(右側金字塔單數)
b = x*2
c = x
while i <= x*2-1:
    if i <= x:
        print('{:>{}}'.format(i*"*",c))
        i += 1
    if i <= x*2 and i > x:
       print('{:>{}}'.format((b-i)*"*",c))
       i += 1
"""
"""
(中間金字塔全數)
while i <= x:
    if x % 2 == 1:
        if i % 2 == 1:
            print(*'{:^{}}'.format(i*"*",x))
        if i % 2 == 0:
            print(" ",end="")
            print(*'{:^{}}'.format(i*"*",x))
        i += 1
    if x % 2 == 0:
        if i % 2 == 1:
            print(" ",end="")
            print(*'{:^{}}'.format(i*"*",x))
        if i % 2 == 0:
            print(*'{:^{}}'.format(i*"*",x))
        i += 1
"""
"""
(中間倒立金字塔全數)
b = x
while x >= i:
    if b % 2 == 1:
        if x % 2 == 1:
            print(*'{:^{}}'.format(x*"*",b))
        if x % 2 == 0:
            print(" ",end="")
            print(*'{:^{}}'.format(x*"*",b))
        x -= 1
    if b % 2 == 0:
        if x % 2 == 1:
            print(" ",end="")
            print(*'{:^{}}'.format(x*"*",b))
        if x % 2 == 0:
            print(*'{:^{}}'.format(x*"*",b))
        x -= 1
"""
"""
(左側金字塔全數)
b = x*2
z = int()
while i <= x*2-1:
    if i <= x:
        if i % 2 == 1:
            str = " "
            seq = (z*"*")
            print(str.join(seq))
        if i % 2 == 0:
            z += (i % 2)+1
            str = "*"
            seq = (z*" ")
            print(str.join(seq))
        i += 1
    if i < x*2 and i > x:
        if i % 2 == 1:
            z -= (i % 2)
            str = " "
            seq = ((z)*"*")
            print(str.join(seq))
        if i % 2 == 0:
            str = "*"
            seq = ((z)*" ")
            print(str.join(seq))
        i += 1
"""
"""
(右側金字塔全數)
b = x*2
z = int()
c = x
s = int(x/2)
while i <= x*2:
    if x % 2 == 1:
        if i <= x:
            if i % 2 == 1:
                str = " "
                seq = (z*"*")
                print('{:>{}}'.format(str.join(seq),c))
            if i % 2 == 0:
                z += (i % 2)+1
                str = "*"
                seq = (z*" ")
                print('{:>{}}'.format(str.join(seq),c))
            i += 1
        if i < x*2 and i > x:
            if i % 2 == 1:
                z -= (i % 2)
                str = " "
                seq = ((z)*"*")
                print('{:>{}}'.format(str.join(seq),c))
            if i % 2 == 0:
                str = "*"
                seq = ((z)*" ")
                print('{:>{}}'.format(str.join(seq),c))
            i += 1
    if x % 2 == 0:
        if i <= x-1:
            if i % 2 == 1:
                str = " "
                seq = (z*"*")
                print('{:>{}}'.format(str.join(seq),c))
            if i % 2 == 0:
                z += (i % 2)+1
                str = "*"
                seq = (z*" ")
                print('{:>{}}'.format(str.join(seq),c))
            i += 1
            if i == x:
                z += 1
                str = " "
                seq =((z-1)*"*")
                print('{:<{}}'.format(str.join(seq),c))
                i += 1
        if i < x*2 and i > x-1:
            if i % 2 == 1:
                z -= (i % 2)
                str = " "
                seq = ((z)*"*")
                print('{:>{}}'.format(str.join(seq),c))
            if i % 2 == 0:
                str = "*"
                seq = ((z)*" ")
                print('{:>{}}'.format(str.join(seq),c))
            i += 1
"""
    
