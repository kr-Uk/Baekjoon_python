import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -sys.maxsize
minimum = sys.maxsize

def dfs(cnt, result):
    global maximum
    global minimum
    
    if cnt == n-1:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return
    
    if op[0] != 0:
        op[0] -= 1
        dfs(cnt+1, result+nums[cnt+1])
        op[0] += 1
    if op[1] != 0:
        op[1] -= 1
        dfs(cnt+1, result-nums[cnt+1])
        op[1] += 1
    if op[2] != 0:
        op[2] -= 1
        dfs(cnt+1, result*nums[cnt+1])
        op[2] += 1
    if op[3] != 0:
        op[3] -= 1
        dfs(cnt+1, int(result/nums[cnt+1]))
        op[3] += 1

dfs(0, nums[0])
print(maximum)
print(minimum)