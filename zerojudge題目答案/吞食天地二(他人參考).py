from sys import stdin
from itertools import accumulate as acc
for s in stdin:
    n,m = map(int,s.split())
    arr = [[0]*(n+1)]
    for i in range(n):
        tRow = [int(x) for x in stdin.readline().split()]#讀入值且轉成int
        tRow = acc([0] + tRow)#將值由左加去右
        pRow = arr[-1]
        pRow = [a + b for a, b in zip(tRow,pRow)]#將值有上往下加
        arr.append(pRow)
    #for row in arr:print(row)
    for i in range(m):
        s = stdin.readline()
        y1,x1,y2,x2 = map(int,s.split())
        r = arr[y2][x2] - arr[y2][x1-1] - arr[y1-1][x2]#減去部份
        r += arr[y1-1][x1-1]#加被扣2次的值
        print(r)