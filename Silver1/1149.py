"""
dp인듯 !
연속된 색 x
R R
R G G
R G R G R // O
"""

import sys
input = sys.stdin.readline

n = int(input())

rgb = [list(map(int, input().split()) for _ in range(n))]
dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        pass