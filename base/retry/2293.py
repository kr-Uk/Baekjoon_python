"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input())

value = 0
answer = 0
idx = 0
    
def dfs():
    global value
    global answer
    global idx
    
    if value == k:
        answer += 1
        return
    
    if value > k:
        return
    
    for i in range(idx, n):
        value += coins[i]
        dfs()
        value -= coins[i]
        idx = i+1
        
dfs()
print(answer)
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
coins = [0] * n
dp = [0] * (k+1)

for i in range(n):
    coins[i] = int(input())
    
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])

"""
dp[0] = 0
dp[1] = 1
dp[2] = 11, 2
dp[3] = 111, 12
dp[4] = 1111, 121, 22
dp[5] = 11111, 1211, 221, 5 dp[1]
dp[n] = dp[n-coins[0]] + dp[n-coins[1]] + .. 
- dp[coins[1] - coins[0]]
코인 하나 추가할 때의 경우의 수 12 21 이거를 어캐 구분할래

1 2 5

1을 만드는건 하나 1
2를 만드는건 11 2
3을 만드는건 2를 만드는거에서 1씩 덧붙힘. 1을 만드는거에서 2를 덧붙힘 겹ㅊ는거 제외
"""