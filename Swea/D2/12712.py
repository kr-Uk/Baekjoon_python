MSG_FORMAT = '#{} {}'
t = int(input())

def sol(ilst, y, x, m):
    cross_result, x_result = ilst[y][x], ilst[y][x]
    cross_dx = [1, -1, 0, 0]
    cross_dy = [0, 0, -1, 1]
    x_dx = [1, -1, 1, -1]
    x_dy = [1, -1, -1, 1]
    
    for i in range(4):
        cross_nx = cross_dx[i]
        cross_ny = cross_dy[i]
        x_nx = x_dx[i]
        x_ny = x_dy[i]
        for j in range(m-1):
            if 0 <= y+cross_ny < n and 0 <= x+cross_nx < n:
                cross_result += ilst[y+cross_ny][x+cross_nx]
                cross_nx += cross_dx[i]
                cross_ny += cross_dy[i]
            if 0 <= y+x_ny < n and 0 <= x+x_nx < n:
                x_result += ilst[y+x_ny][x+x_nx]
                x_nx += x_dx[i]
                x_ny += x_dy[i]
    
    return max(cross_result, x_result)

for test_case in range(1, t+1):
    answer = 0
    n, m = map(int, input().split())
    ilst = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            answer = max(answer, sol(ilst, i, j, m))
    
    print(MSG_FORMAT.format(test_case, answer))