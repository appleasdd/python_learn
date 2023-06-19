from sys import stdin
for s in stdin:
    n = int(s)
    arr = [int(x) for x in stdin.readline().split()]
    """將值寫入arr"""
    arr.sort(key = lambda z:(z%10,-z))
    print(*arr)
