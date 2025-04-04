"""
연속된 색 x
R R
R G G
R G R G R // O
모든 경우의 수를 빠르게 확인..?
최소 비용 신장 트리,,
[26 40 83]
[49+40 60+26 57+26]
[13+57+26 89+57+26 99+60+26]
"""

import sys
input = sys.stdin.readline

n = int(input())
rgb = [[] for _ in range(n)]
rgb[0] = list(map(int, input().split()))

for i in range(1, n):
    rgb[i] = list(map(int, input().split()))
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[n-1]))