MSG_FORMAT = '#{} {}'
from collections import deque

def bfs(node):
    q = deque([node])
    visited = set([node])
    last_level = []
    while q:
        level_size = len(q)
        curr_level = []
        for _ in range(level_size):
            curr = q.popleft()
            curr_level.append(curr)
            if curr in graph.keys():
                for g in graph[curr]:
                    if g not in visited:
                        visited.add(g)
                        q.append(g)
        last_level = curr_level
    return max(last_level)
        
            
            

for t in range(1, 11):
    n, start = map(int, input().split())
    graph = {}
    data = list(map(int, input().split()))
    graph = {}
    for i in range(0, n, 2):
        u, v = data[i], data[i + 1]
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    print(MSG_FORMAT.format(t, bfs(start)))