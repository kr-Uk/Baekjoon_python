"""
연결 요소 개수

graph
1: [2, 5]
2: [1, 5]
3: [4]
4: [3, 6]
5: [2, 1]
6: [4]

그냥 dfs 돌면서 하면 되지 않나..?
"""

from collections import deque
import sys
sys.setrecursionlimit(10**6) # 이거 없으면 런타임 에러 뜸
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in graph[start]:
       if not visited[i]:
           dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[0] = True
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        count += 1
        
print(count)