"""
그냥 규칙 찾아서 점화식 DP
1 1 1 2 2 3 4 5 7 9
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2 = dp[1] + dp[2]
dp[5] = 2 = dp[2] + dp[3]
dp[6] = 3 = dp[3] + dp[4]
...
dp[n] = dp[n-2] + dp[n-3]
"""

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

t = int(input())
for _ in range(t):
    print(dp[int(input())])