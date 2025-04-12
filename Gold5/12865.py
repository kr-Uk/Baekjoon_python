"""
백트래킹 !

당연히 보자마자 백트래킹인줄 알았는데 시간초과,,
DP문제임 !
아래는 recursion 풀이

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
result = 0

def dfs(idx, weight, value):
    global result
    
    if weight > k:
        return
    
    if idx == n:
        result = max(result, value)
        return
    
    dfs(idx + 1, weight + wv[idx][0], value + wv[idx][1])
    dfs(idx + 1, weight, value)
            
dfs(0, 0, 0)
print(result)
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)


