while True:
    try:
        x = int(input())
        z = int()
        def f(x):
            if x == 1:
                return 1
            elif x >= 2:
                z = x + f(x-1)
                return z
        def g(x):
            if x == 1:
                return 1
            if x >= 2:
                return f(x) + g(x-1)
        f(x)
        g(x)
        print(f(x),g(x))    
    except :
        break 