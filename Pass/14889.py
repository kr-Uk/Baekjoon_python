import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

score = []
n = int(input())
member = set([i for i in range(n)])
link = set([])
start = set([])
result = sys.maxsize
for _ in range(n):
    score.append(list(map(int, input().split())))
    
def dfs(cnt, idx):
    global start
    global link
    global result
    if cnt == n // 2:
        link = member - start
        first_team = list(link)
        second_team = list(start)
        tmp = 0
        for i in range(cnt):
            for j in range(i+1, cnt):
                tmp += score[first_team[i]][first_team[j]]
                tmp += score[first_team[j]][first_team[i]]
                tmp -= score[second_team[i]][second_team[j]]
                tmp -= score[second_team[j]][second_team[i]]
        
        result = min(result, abs(tmp))
        return
    
    for i in range(idx, n):
        start.add(i)
        dfs(cnt+1, i+1)
        start.remove(i)
        
dfs(0, 0)
print(result)