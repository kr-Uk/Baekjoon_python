n = int(input())
wine = [0] * n
for i in range(n):
    wine[i] = int(input())

dp = [0] * 10001
dp[0] = wine[0]
if n > 1:
    dp[1] = wine[0] + wine[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])

print(dp[n-1])