"""
dp 계단문제 느낌?
계단 문제는 n번째 계단을 무조건 밟는데 이거는 다 고려해야해

1. i번 째랑 i-1번 째 마시고, i-3까지 마신 총 와인: dp[i] = wine[i] + wine[i-1] + dp[i-3]
2. i번 째랑 i-2번 째까지 마신 총 와인 dp[i] = wine[i] + dp[i-2]
3. i-1번 째까지 마신 총 와인 dp[i] = dp[i-1]

"""

import sys
input = sys.stdin.readline

n = int(input())
wine = [0] * n
dp = [0] * n

for i in range(n):
    wine[i] = int(input())
    if i == 0:
        dp[0] = wine[0]
    if i == 1:
        dp[1] = wine[1] + wine[0]
    if i == 2:
        dp[2] = max(wine[2] + wine[1], wine[0] + wine[2], dp[1])
    
for i in range(3, n):
    dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + dp[i-2], dp[i-1])

print(dp[n-1])