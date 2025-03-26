"""
n = 5
m = 5
start = 3

[2, 3]
[1, 5]
[1, 4]
[3, 5]
[2, 4]

dfs
visited = [0 1 1 1 1 1] 방문한 노드

bfs
visited = [0 1 1 1 1 1] 방문한 노드
q = [] 방문할 노드
"""

import sys
from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end = " ")
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    
    while q:
        curr = q.popleft()
        if not visited[curr]:
            visited[curr] = True
            print(curr, end = " ")
            q.extend(graph[curr])

n, m, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (n+1)
dfs(start)

print()

visited = [False] * (n+1)
bfs(start)