import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(x):
    visited[x] = 1
    print(x, end = " ")
    for i in range(1, n+1):
        if visited[i] == 0 and graph[x][i] == 1:
            dfs(i)

def bfs(x):
    q = deque([])
    q.append(x)
    visited[x] = 1
    while q:
        tmp = q.popleft()
        print(tmp, end = " ")
        for i in range(1, n+1):
            if visited[i] == 0 and graph[tmp][i] == 1:
                q.append(i)
                visited[i] = 1

visited = [0] * (n+1)  
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)