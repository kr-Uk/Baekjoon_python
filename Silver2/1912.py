"""
dp ?
10 -4 3 1 5 6 -35 12 21 -1

dp[0] = 10
10이 -4보다 크니까 dp[1] = dp[0] - 4
dp[2] = dp[1] + 3
dp[3] = dp[2] + 1
dp[4] = dp[3] + 5
dp[5] = dp[4] + 6
dp[6] = dp[5]가 -35보다 작으니까 dp[6] = dp[5]
dp[7] = 12
dp[8] = dp[7] + 21
...

다 음수일 때 처리
0이 진짜 맥스일 때 처리

애초에 dp를 잘못한듯..!
elif (dp[i-1] + seq[i]) < 0:
        dp[i] = 0
이 부분이 잘못됬다
"""

import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]
seq = list(map(int, input().split()))
dp[0] = seq[0]

for i in range(1, len(seq)):
    dp[i] = max(seq[i], dp[i-1] + seq[i])

print(max(dp))