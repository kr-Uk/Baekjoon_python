# 2667
# 왜 틀려 ㅜㅜ

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
  graph.append(list(map(int, input().strip())))

def bfs(x, y):
    q = deque([])
    q.append((y, x))
    graph[y][x] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = cnt
                q.append((nx, ny))

result = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
        cnt = 2
        bfs(i, j)
        cnt += 1

print(len(result))
result.sort()
for r in result:
    print(r)

print(graph)