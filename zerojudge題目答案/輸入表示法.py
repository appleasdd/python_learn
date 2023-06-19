while True:
    try:
        print("%10.3d"%(45))
        t = "%r%r%r"
        print(t%(1,2,3))
        y = "{} + {} = {}"
        print(y.format(1,2,3))
        print("姓名:{}".format(45))
        print("姓名:%d"%(45))
        print(f"a{4+8}")
    except:
        break