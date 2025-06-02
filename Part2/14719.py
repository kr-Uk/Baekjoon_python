h, w = map(int, input().split())
graph = [[0] * w for _ in range(h)]
wall = list(map(int, input().split()))
result = 0
isOne = False

for i in range(w):
    for j in range(wall[i]):
        graph[j][i] = 1

for i in range(h):
    isOne = False
    for j in range(w):
        if graph[i][j] == 1:
            isOne = True
        tmp = 0
        while graph[i][j] == 0 and isOne:
            tmp += 1
            if j == w-1:
                break
        result += tmp

print(result)
        