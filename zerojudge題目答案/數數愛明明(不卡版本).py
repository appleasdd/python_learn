while True:
  try:
    f=[0,1]
    g=[0,1]
    n = int(input())

    for k in range(2,n+1):
      f.append(k+f[k-1])
    
    for k in range(2,n+1):
      g.append(f[k]+g[k-1])

    print(f[n], g[n])
  
  except:
    break
    