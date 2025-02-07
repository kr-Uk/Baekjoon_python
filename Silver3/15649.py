"""
가장 먼저 생각난 것은 nPm
파이썬 내장함수로도 풀 수 있고
백트래킹으로 풀 수 있다.

from itertools import permutations

n, m = map(int, input().split())

p = permutations(range(1, n+1), m)

for i in p:
    print(" ".join(map(str, i)))
    
"""

n, m = map(int, input().split())
ans = []

def backTracking():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            backTracking()
            ans.pop()

backTracking()