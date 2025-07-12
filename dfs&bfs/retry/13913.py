import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

if k <= n:
    print(n-k)
    for i in range(n, k-1, -1):
        print(i, end=" ")
    exit(0)

MAX = 100001
visited = [1e9] * MAX

q = deque([(n, 0, [n])])
visited[n] = 0

while q:
    curr, count, moving = q.popleft()
    
    if curr == k:
        print(count)
        for move in moving:
            print(move, end=" ")
        break
    
    for next in (curr-1, curr+1, curr*2):
        if 0 <= next < MAX:
            if visited[next] >= count + 1:
                tmp = moving.copy()
                tmp.append(next)
                visited[next] = count + 1
                q.append((next, count + 1, tmp))