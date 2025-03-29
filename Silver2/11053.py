"""
a = 5 2 1 10 3 9 4
seq = [5, 10] [2, 10] [1, 10]
"""

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
seq = [0] * n

for i in a:
    if i == 0:
        seq[i] = a[i]
    