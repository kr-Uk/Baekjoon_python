"""
백트래킹으로 해보기
"""

def dfs():
    if len(q) == m:
        for i in q:
            print(i, end = " ")
        print()
        return 0
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            q.append(i)
            dfs()
            q.pop()
            visited[i] = False
            
n, m = map(int, input().split())
seq = [i for i in range(1, n+1)]
visited = [False] * (n+1)
q = []

dfs()