import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque([n])
    while q:
        curr = q.popleft()
        if not visited[curr]:
            visited[curr] = True
            q.extend(graph[curr])

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        result += 1
        
print(result)