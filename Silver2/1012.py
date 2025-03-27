"""
미리 1로 만들어 놓고 조건문?
2줄씩 더 만들자,,
10 8 17
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 3 ...
아ㅏ 이렇게 하면 그 사이에 있는게 카운트될 수도 있구나
"""

"""
BFS 또는 DFS를 하는 문제구나,, !!
"""

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    
    count = 0
    for _y in range(m):
        for _x in range(n):
            if graph[_x][_y] == 1:
                dfs(_y, _x)
                count += 1

    print(count)