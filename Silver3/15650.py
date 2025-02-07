"""
가장 먼저 생각난 것은 nCm
파이썬 내장함수로도 풀 수 있고
백트래킹으로 풀 수 있다.

from itertools import combinations

n, m = map(int, input().split())

p = combinations(range(1, n+1), m)

for i in p:
    print(" ".join(map(str, i)))
        
"""

n, m = map(int, input().split())
ans = []

def backTracking(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            backTracking(i+1)
            ans.pop()

backTracking(1)