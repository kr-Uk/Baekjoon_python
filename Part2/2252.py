import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
q = deque([])
result = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

for i in range(n):
    if len(q) == 0:
        print("Cycle")
        exit(0)
    
    curr = q.popleft()
    result[i] = curr
    
    for g in graph[curr]:
        degree[g] -= 1
        if degree[g] == 0:
            q.append(g)

for r in result:
    print(r, end=" ")