"""
타일링은 거의 대부분 DP

dp[1] = 1
dp[2] = 2
dp[3] = dp[1]에서 2개 채우기 + dp[2]에서 1개 채우기
      = dp[1] * 2 + dp[2]
여기서 다 세우는게 겹침
따라서 dp[1] + dp[2]
"""

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])