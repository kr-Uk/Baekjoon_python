"""
bfs 또는 dfs
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and uginong[ny][nx] == 1:
            uginong[ny][nx] = 0
            dfs(ny, nx)
    

for _ in range(t):
    m, n, k = map(int, input().split())
    uginong = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a, b = map(int, input().split())
        uginong[b][a] = 1
    for y in range(n):
        for x in range(m):
            if uginong[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)