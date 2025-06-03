h, w = map(int, input().split())
graph = [[0] * w for _ in range(h)]
wall = list(map(int, input().split()))
result = 0

for i in range(w):
    for j in range(wall[i]):
        graph[j][i] = 1

for i in range(h):
    start = False
    tmp = 0
    for j in range(w):
        if graph[i][j] == 1:
            start = True
            result += tmp
            tmp = 0
        if graph[i][j] == 0 and start:
            tmp += 1
            
print(result)