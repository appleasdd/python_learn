from sys import stdin #連續輸入
for s in stdin:
    n = int(s)
    if (n==0):
        break #遇到0結束
    b = bin(n) #轉成2進位
    len1 = len(b) #原字串長度
    len2 = len(b.rstrip('1'))#消除右邊出現的1碰到0結束
    print(len1 - len2)
