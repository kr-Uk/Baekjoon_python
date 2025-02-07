"""
어느 칸에서 올라왔을까?
stair[n] 전칸 or 전전칸
전칸인 경우 stair[n] + stair[n-1] + DP(n-3) // 연속 불가능
전전칸인 경우 stair[n] + DP(n-2)
"""

dp = [0] * 301
stair = [0] * 301

n = int(input())
for i in range(1, n+1):
    stair[i] = int(input())
    if i == 1:
        dp[1] = stair[1]
    elif i == 2:
        dp[2] = stair[1] + stair[2]
    elif i == 3:
        dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])
    dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])

print(dp[n])