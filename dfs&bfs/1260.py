import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
    
def dfs(start):
    visited[start] = True
    print(start, end = " ")
    
    for g in graph[start]:
        if not visited[g]:
            dfs(g)
            
def bfs(start):
    q = deque([start])
    
    while q:
        curr = q.popleft()
        if not visited[curr]:
            visited[curr] = True
            print(curr, end = " ")
            q.extend(graph[curr])

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)