MSG_FORMAT = '#{} {}'
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False]*100 for _ in range(100)]
    visited[y][x] = 0
    dx = [1, -1, 0]
    dy = [0, 0, 1]
    while q:
        x, y = q.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if ladder[ny][nx] == 2:
                    return 1
                elif ladder[ny][nx] == 1 and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    break
    return 0

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i] == 1:
            if bfs(i, 0):
                print(MSG_FORMAT.format(t, i))
                break
        