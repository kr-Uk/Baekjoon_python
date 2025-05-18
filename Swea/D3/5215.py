"""
knapsack 알고리즘 !
2차원 dp
value랑 calory
"""

msg_FORMAT = "#{} {}"
t = int(input())

for c in range(1, t+1):
    n, l = map(int, input().split())
    tk = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (l+1) for _ in range(n+1)]
    
    for i in range(1, n+1): # 물건 개수만큼
        for j in range(1, l+1): # 제한 무게까지
            if j >= tk[i-1][1]: # 칼로리가 제한 칼로리를 넘지 않았을 경우 tk[0][1] = 200
                dp[i][j] = max(tk[i-1][0] + dp[i-1][j-tk[i-1][1]], dp[i-1][j])
                # dp[1][200] 첫 번째 물건까지 제한 무게 200 첫 번째 물건 가치 + 담고 남은 칼로리까지의 가치
            else:
                dp[i][j] = dp[i-1][j]
    
    print(msg_FORMAT.format(c, dp[n][l]))