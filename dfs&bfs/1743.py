import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
result = 0

for _ in range(k):
    x, y = map(int, input().split())
    graph[y-1][x-1] = 1
    
def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    graph[y][x] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        _x, _y = q.popleft()
        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                cnt += 1
                q.append((nx, ny))
    
    return cnt

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            result = max(result, bfs(x, y))

print(result)