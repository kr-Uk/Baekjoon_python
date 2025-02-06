"""
다이나믹 프로그래밍
1은 -1
2는 /2
3은 /3

4는 아무거나 2개
5는 -1, 4
6은 /3 /2
7은 -1 6
"""

n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])