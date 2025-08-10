"""
애초에 입력받을 때 둘레 구하기
flag 선언

아닌거같아,,
가운데 붙히면 안돼
"""

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 101 for _ in range(101)]
coor = []
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))
    
for x, y in coor:
    for i in range(10):
        for j in range(10):
                graph[y+i][x+j] = 1
                
for y in range(101):
    for x in range(101):
        if graph[y][x] == 1:
            temp = 0
            for i in range(4):
                if graph[y+dy[i]][x+dx[i]] == 1:
                    temp += 1
                
            if temp == 3:
                result += 1
            elif temp == 2:
                result += 2
print(result)