"""
2xn일 경우
2x(n-1)에서 한개
2x(n-2)에서 한개 (세우는거는 위에서 포함)
"""

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
print(dp[n] % 10007)