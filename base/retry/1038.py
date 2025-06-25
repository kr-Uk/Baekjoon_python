"""
10
20 21
30 31 32
40 41 42 43
... 9 + 45 + 

210
310 320 321
9876543210
"""

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
answer = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        nums = sorted(list(j), reverse=True)
        answer.append(int("".join(map(str, nums))))

answer.sort()
print(answer[n] if len(answer) > n else -1)