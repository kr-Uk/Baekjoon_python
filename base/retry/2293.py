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
    dp[coins[i]] = 1

for i in range(k):
    for j in range(n):
        if i-coins[j] >= 0:
            dp[i] += dp[i-coins[j]]

print(dp)