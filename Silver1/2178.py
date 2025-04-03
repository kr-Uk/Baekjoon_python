"""
1012번 풀 때 dfs를 갖고와
최단거리는 bfs ..!
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]
        
            
n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    str = input()
    for j in range(m):
        graph[i][j] = int(str[j])
        
print(bfs(0, 0))