"""
미리 1로 만들어 놓고 조건문?
2줄씩 더 만들자,,
10 8 17
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 3 ...
"""

import sys

t = int(input())
result = []

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    ilist = [[0] * (n+2) for _ in range(m+2)]
    count = 0
    
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        if ilist[a+1][b+1] == 0:
            count += 1
        ilist[a+1][b+1] = 1
        ilist[a+1][b+2] = 1
        ilist[a+2][b+1] = 1
        ilist[a+1][b] = 1
        ilist[a][b+1] = 1
    result.append(count)
        
for i in result:
    print(i)
            
