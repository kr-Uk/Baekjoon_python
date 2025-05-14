# 2667

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
    global cnt
    q = deque([])
    q.append((y, x))
    graph[y][x] = 0
    cnt += 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                q.append((ny, nx))

result = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
        cnt = 0
        bfs(j, i)
        result.append(cnt)

result.sort()
print(len(result))
for r in result:
    print(r)