n = int(input())
dp = [0] * (n+1)
seq = list(map(int, input().split()))

dp[0] = seq[0]
if n > 1:
    dp[1] = max(dp[0], seq[0] + seq[1])

