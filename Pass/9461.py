"""
점화식 찾기
dp[n] = d[n-2] + dp[n-3]
"""

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]
    
n = int(input())
for _ in range(n):
    k = int(input())
    print(dp[k])