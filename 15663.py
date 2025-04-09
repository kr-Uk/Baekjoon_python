import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

seq = list(map(int, input().split()))
seq.sort()
visited = [False] * n
result = []
prev = 0

def dfs(a):
    global result
    prev = 0
    
    if a == m:
        for i in result:
                print(i, end=" ")
        print()
        return
    else:
        for i in range(n):
            if not visited[i] and prev != seq[i]:
                prev = seq[i]
                visited[i] = True
                result.append(seq[i])
                dfs(a+1)
                result.pop()
                visited[i] = False

dfs(0)

"""
1 7 9 9
1 9
"""