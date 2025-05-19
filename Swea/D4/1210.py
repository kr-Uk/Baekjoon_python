MSG_FORMAT = '#{} {}'
from collections import deque

def bfs(x, y):
    q = deque([])
    dx = [1, -1, 0]
    dy = [0, 0, 1]
    while q:
        x, y = q.popleft()
        if y == 99:
            if x == 99:
                return 1
            else:
                return 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx] == 1:
                q.append(nx, ny)
                break
            

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i] == 1:
            if bfs(i, 0):
                print(MSG_FORMAT.format(t, i))
                break
        