from sys import stdin
for x in stdin:
    x = list(x)
    x.pop(-1)
    y = list()
    for i in range(len(x)):
        if x[i] == "1"or x[i] =="2"or x[i] =="3"or x[i] =="4"or x[i] =="5"or x[i] =="6"or x[i] == "7"or x[i] =="8"or x[i] == "9":
            x[i] = int(x[i])
            y.append(x[i])
        else:
            asd = x[i]
            for j in range(len(y)):
                for k in range(y[j]):
                    if x[i] == str(asd) and x[i] != "b":
                        print(asd,end="")
                    elif x[i] == "b":
                        print(" ",end="")
            if x[i] == "!":
                print("\n")
            y.clear()
    print("\n")