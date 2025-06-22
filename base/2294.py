"""
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = min(dp[5-5]+1, dp[5-1]+1)
dp[6] =  

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
dp = [100001] * (k+1)
dp[0] = 0

for i in range(n):
    coins[i] = int(input())
    
coins.sort()

for coin in coins:
    for i in range(coin, k+1):
        if i % coin == 0:
            dp[i] = min(dp[i-coin]+1, i // coin)
        else:
            dp[i] = min(dp[coin] + dp[i-coin], dp[i])

print([dp[k], -1][dp[k] in [0, 100001]])