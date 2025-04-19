"""
LCS 알고리즘 적용
"""

str1 = input()
str2 = input()

m = len(str1)
n = len(str2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(m):
    for j in range(n):
        if str1[i] == str2[j]:
            dp[j+1][i+1] = dp[j][i] + 1
        else:
            dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])
            
print(max(dp[n]))