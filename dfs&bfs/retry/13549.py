import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

if k <= n:
    print(n-k)
    exit(0)

MAX = 100001
visited = [1e9] * MAX

q = deque([(n, 0)])
visited[n] = 0
while q:
    curr, count = q.popleft()
    if curr == k:
        print(count)
        break
    
    if 0 <= curr*2 < MAX and visited[curr*2] > count:
        visited[curr*2] = count
        q.appendleft((curr*2, count))
        
    for next in (curr-1, curr+1):
        if 0 <= next < MAX:
            if visited[next] > count + 1:
                visited[next] = count + 1
                q.append((next, count + 1))
                