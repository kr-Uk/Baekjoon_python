"""
dp
n이면 dp[n-1] + dp[n-2] + dp[n-3]
"""

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
n = int(input())
for _ in range(n):
    k = int(input())
    print(dp[k])