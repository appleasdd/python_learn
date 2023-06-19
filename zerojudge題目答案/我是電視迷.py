from sys import stdin
for x in stdin:
    x = x.split(" ")
    x = list(map(int,x))
    z = int()
    z = ((x[1]-x[0])+100)%100
    print(z)

                
        
    
            
