import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

if k <= n:
    print(n-k)
    print(1)
    exit(0)

MAX = 100001
visited = [1e9] * MAX
result = [1e9, 0]

q = deque([(n, 0)])
visited[n] = 0

while q:
    curr, count = q.popleft()
    if count > result[0]:
        continue
    
    if curr == k:
        if count < result[0]:
            result[0] = count
            result[1] = 1
        elif count == result[0]:
            result[1] += 1
        continue
    
    for next in (curr-1, curr+1, curr*2):
        if 0 <= next < MAX:
            if visited[next] >= count + 1:
                visited[next] = count + 1
                q.append((next, count + 1))
    
for r in result:
    print(r)