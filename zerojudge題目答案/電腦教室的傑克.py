from sys import stdin
for x in stdin:
    if x != "\n":
        x = int(x)
        for i in range(x):
            y = input()
            y = y.split()
            y = list(map(int,y))
            r = ((y[0]-0)+(y[1]-0))**0.5
            yee = 100 - (r * r)
            if 0 < yee <= 30:
                print("sad!")
            elif 30 < yee <= 60:
                print("hmm~~") 
            elif 60 < yee < 100:
                print("Happyyummy")
            else:
                print("evil!!")
        
                
        