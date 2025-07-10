import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    cnt = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < m+1 and 0 < ny < n+1 and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

n, m, k = map(int, input().split())
graph = [[0] * (m+1) for _ in range(n+1)]
result = 0

for _ in range(k):
    col, row = map(int, input().split())
    graph[col][row] = 1

for x in range(1, m+1):
    for y in range(1, n+1):
        if graph[y][x] == 1:
            graph[y][x] = 0
            result = max(result, bfs(x, y))

print(result)