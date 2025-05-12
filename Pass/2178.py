# 2178

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().strip())))

def bfs(x, y):
  q = deque([])
  q.append((y, x))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
        graph[ny][nx] = graph[y][x] + 1
        q.append((nx, ny))

bfs(0, 0)
print(graph[n-1][m-1])