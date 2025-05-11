import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if seq[i-1] < seq[j-1]:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

result = 1
for i in range(n+1):
    result = max(max(dp[i]), result)

print(result)
print(dp)

"""
0 1 2 1 3 2 5
1 0 1 1 1 1 1
2 0 1 1 2 2 2
1 0 1 1 2 3 3
3 0 1 1 2 3 4
2 0 1 1 2 3 4
5 0 1 1 2 3 4
"""