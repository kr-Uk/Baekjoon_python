MSG_FORMAT = '#{} {}'
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, power, n):
    global result
    if cnt == 7:
        result.add(n)
        print(n)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            new_n = n + graph[ny][nx] * (10**power)
            dfs(nx, ny, cnt+1, power+1, new_n)

for test_case in range(1, t+1):
    graph = [list(map(int, input().split())) for _ in range(4)]
    result = set([])
    for x in range(4):
        for y in range(4):
            dfs(x, y, 1, 1, graph[y][x])
    
    print(MSG_FORMAT.format(test_case, len(result)))