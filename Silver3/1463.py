"""
다이나믹 프로그래밍
단순히 i-1값에 1을 더한 값보다
2 또는 3으로 나눈 값에 1을 더한 값이 더 작으면
그걸로 바꿈
"""

n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])