while True:
  try:
      x = input()
      x = list(map(int,x))
      a = int()
      s = int()
      d = int()
      for i in range(len(x)):
          if i % 2 == 0:
              s += x[i]
          if i % 2 == 1:
              d += x[i]
      if s >= d:
          a = s - d
      elif s < d:
          a = d - s
      print(a)
  
  except:
    break
