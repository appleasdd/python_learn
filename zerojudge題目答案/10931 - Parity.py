while True:
    try:
        x = int(input())
        if x == 0:
            break
        x = list(bin(x))
        y = x.count("1")
        x.pop(0)
        x.pop(0)
        z = "".join(x)
        print("The parity of {} is {} (mod 2).".format(z,y))
    except:
        break