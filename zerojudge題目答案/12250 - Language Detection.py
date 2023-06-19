i = int()
while True:
    x = input()
    if x == "#":
        break
    x = list(x)
    if x[-1] == " ":
        x.pop(-1)
    x = "".join(x)
    i += 1
    if x == "HELLO":
        print("Case {}: ENGLISH".format(i))
    elif x == "HOLA":
        print("Case {}: SPANISH".format(i))
    elif x == "HALLO":
        print("Case {}: GERMAN".format(i))
    elif x == "BONJOUR":
        print("Case {}: FRENCH".format(i))
    elif x == "CIAO":
        print("Case {}: ITALIAN".format(i))
    elif x == "ZDRAVSTVUJTE":
        print("Case {}: RUSSIAN".format(i))
    else:
        print("Case {}: UNKNOWN".format(i))
    
    