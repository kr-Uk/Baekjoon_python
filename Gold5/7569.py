"""
저번에 토마토는 2차원
이번엔 3차원!
bfs 고고

"""

from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque([])

dz = [-1, 1, 0, 0, 0, 0] # 위아래
dy = [0, 0, -1, 1, 0, 0] # 앞뒤
dx = [0, 0, 0, 0, -1, 1] # 좌우

def bfs():
    while q:
        curr = q.popleft()
        z, y, x = curr[0], curr[1], curr[2]
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    q.append((nz, ny, nx))
    
for i in range(m):
    for j in range(n):
        for k in range(h):
            if graph[k][j][i] == 1:
                q.append((k, j, i))

bfs()

result = 0
for k in graph:
    for j in k:
        for i in j:
            if i == 0:
                print(-1)
                exit(0)
            result = max(result, i)
print(result - 1)



