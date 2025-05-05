from collections import deque

n = int(input())
m = int(input())
computer = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

def bfs():
    global cnt
    q = deque([])
    q.append(1)
    visited[1] = True
    while q:
        tmp = q.popleft()
        for i in range(1, n+1):
            if computer[tmp][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

for _ in range(m):
    a, b = map(int, input().split())
    computer[a][b] = 1
    computer[b][a] = 1
    
bfs()
print(cnt)