"""
DP

1 a[1]은 1
2 a[2]는 1+1, 2
4 a[3]은 1+1+1, 1+2, 2+1, 3
7 a[4]는 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1

"""

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())

for _ in range(t):
    print(dp[int(input())])
