import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(cnt, result):
    global maximum
    global minimum
    
    if cnt == n-1:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    
    if op[0] > 0:
        op[0] -= 1
        dfs(cnt+1, result+numbers[cnt+1])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(cnt+1, result-numbers[cnt+1])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(cnt+1, result*numbers[cnt+1])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(cnt+1, int(result/numbers[cnt+1]))
        op[3] += 1

dfs(0, numbers[0])
print(maximum)
print(minimum)