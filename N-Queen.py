"""
import sys
sys.setrecursionlimit(10**9)

n = int(input())
threaten = []
result = 0

def isPossible(y, x):
    for _y, _x in threaten:
        if abs(y - _y) == abs(x - _x) or x == _x:
            return False
    return True

def dfs(idx, cnt):
    global result
    
    if cnt == n:
        result += 1
        return
    
    for j in range(n):
        if isPossible(idx, j):
            threaten.append((idx, j))
            dfs(idx+1, cnt+1)
            threaten.remove((idx, j))
                
dfs(0, 0)
print(result)
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
cols = [False] * n
diagPlus = [False] * (n*2-1)
diagMinus = [False] * (n*2-1)

result = 0

def dfs(y):
    global result
    
    if y == n:
        result += 1
        return
    
    for x in range(n):
        if not cols[x] and not diagPlus[x+y] and not diagMinus[y-x+n-1]:
            cols[x] = True
            diagPlus[x+y] = True
            diagMinus[y-x+n-1] = True
            dfs(y+1)
            cols[x] = False
            diagPlus[x+y] = False
            diagMinus[y-x+n-1] = False
                   
dfs(0)
print(result)