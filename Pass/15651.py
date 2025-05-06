def dfs():
    if len(q) == m:
        for i in q:
            print(i, end = " ")
        print()
        return 0
    
    for i in range(1, n+1):
        q.append(i)
        dfs()
        q.pop()
            
n, m = map(int, input().split())
seq = [i for i in range(1, n+1)]
q = []

dfs()