from sys import stdin
for x in stdin:
    x = x.split(" ")
    x = list(map(int,x))
    if x[0] == 0 or x[1] == 0:
        print("Go Kevin!!")
    elif x[0] % x[1] == 1:
        print("Go Kevin!!")
    else:
        print("No Stop!!")

                
        
    
            
