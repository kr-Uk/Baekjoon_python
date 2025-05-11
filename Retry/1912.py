n = int(input())
dp = [0] * (n+1)
seq = list(map(int, input().split()))
dp[1] = seq[0]

for i in range(1, n+1):
    dp[i] = max(dp[i-1]+seq[i-1], seq[i-1])

print(max(dp))