"""
bfs 또는 dfs!
dfs는 recursion이라 한번에 진행하기는 힘들듯..?
bfs로 큐 이용 !

[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 1, 1]
"""

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
q = deque()
result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

def bfs():
    dx = [-1, 1, 0, 0] # 상하
    dy = [0, 0, -1, 1] # 좌우
    
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for i in range(4):
                nx = curr[0] + dx[i]
                ny = curr[1] + dy[i]
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                    box[nx][ny] = box[curr[0]][curr[1]] + 1
                    q.append((nx, ny))

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)