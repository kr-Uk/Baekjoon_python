from collections import deque
MSG_FORMAT = '#{} {}'

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * 16 for _ in range(16)]
    visited[y][x] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[ny][nx] == 3:
                    return 1
                elif maze[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
    return 0

for _ in range(10):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(1, 15):
        for j in range(1, 15):
            if maze[i][j] == 2:
                print(MSG_FORMAT.format(t, bfs(j, i)))
                break