import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
tmp = []
w_graph = [[0] * n for _ in range(m)]
b_graph = [[0] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
w_result = 0
b_result = 0

for _ in range(m):
    tmp.append(list(input().rstrip()))

for i in range(m):
    for j in range(n):
        if tmp[i][j] == 'W':
            w_graph[i][j] = 1
        else:
            b_graph[i][j] = 1


def w_bfs(x, y):
    cnt = 0
    w_graph[y][x] = 0
    q = deque([(x, y)])
    while q:
        cnt += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and w_graph[ny][nx] == 1:
                q.append((nx, ny))
                w_graph[ny][nx] = 0
    return cnt

def b_bfs(x, y):
    cnt = 0
    b_graph[y][x] = 0
    q = deque([(x, y)])
    while q:
        cnt += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and b_graph[ny][nx] == 1:
                q.append((nx, ny))
                b_graph[ny][nx] = 0
    return cnt

for i in range(m):
    for j in range(n):
        if w_graph[i][j] == 1:
            w_result += (w_bfs(j, i))**2
        if b_graph[i][j] == 1:
            b_result += (b_bfs(j, i))**2

print(w_result, b_result)