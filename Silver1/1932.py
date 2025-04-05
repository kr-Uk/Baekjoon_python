"""
그냥 다 합치면 되는 거 아녀?
dp로 쭉 합치면서 내려와

7 0번
3 8 1번
8 1 0 2번 인덱스
[2][0] += [1][0]
[2][2] += [1][1]
[2][1] += min([1][0], [1][1])
2 7 4 4
...
"""

import sys
input = sys.stdin.readline

n = int(input())
triangle = [[] for _ in range(n)]

for i in range(n):
    triangle[i] = list(map(int, input().split()))

for i in range(1, n):
    triangle[i][0] += triangle[i-1][0]
    triangle[i][i] += triangle[i-1][i-1]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))