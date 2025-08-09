import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 100 for _ in range(100)]
coor = []
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))
    
for x, y in coor:
    for i in range(10):
        for j in range(10):
            if graph[y+i][x+j] == 0:
                graph[y+i][x+j] = 1

for y in range(100):
    for x in range(100):
        if graph[y][x] == 1:
            result += 1
            
print(result)