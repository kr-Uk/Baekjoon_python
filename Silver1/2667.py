"""
이거는 1012번이랑 비슷함
0 -1 -1
0 -1 -1
-1 -1 -1
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    
    graph[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 1:
            cnt += dfs(nx, ny)
    return cnt

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
sum = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            sum.append(dfs(i, j))
            
sum.sort()
print(len(sum))
for i in sum:
    print(i)