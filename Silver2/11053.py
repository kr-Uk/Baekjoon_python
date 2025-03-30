"""
a = 5 2 1 9 10 3 5 4
5부터 시작 => 1개 dp[0] = 1
2 : 5보다 작으므로 => 1개 dp[1] = 1
1 : 2보다 작으므로 => 1개 dp[2] = 1
9 : 5, 2, 1보다 큼 => 비교하기 => 2개 dp[3] = 2
...
"""

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if (a[i] > a[j]) and (dp[i] < dp[j]):
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))