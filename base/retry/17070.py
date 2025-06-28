"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

graph = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
dx = [1, 0, 1]
dy = [0, 1, 1]

def dfs(isWidth, isHeight, x, y):
    global cnt
    
    if x == n-1 and y == n-1:
        cnt += 1
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0:
            if i == 0 and isWidth:
                dfs(True, False, nx, ny)
            if i == 1 and isHeight:
                dfs(False, True, nx, ny)
            if i == 2 and graph[ny-1][nx] == 0 and graph[ny][nx-1] == 0:
                dfs(True, True, nx, ny)
        
    
dfs(True, False, 1, 0)
print(cnt)
"""
"""
DP로 풀어보기
"""

import sys
input = sys.stdin.readline

graph = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
