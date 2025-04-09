"""
일단 완전 탐색,,
combination으로 나눈 경우의 수 다 탐색해서 차이 제일 작은 것 ㄱㄱ
왜인지 모르겠는데, (0, n), (1, n-1) 이런 식으로 인덱스끼리 묶어서 비교할 수 있어,,

import sys
import itertools
input = sys.stdin.readline

n = int(input())
s = [[0]*n for _ in range(n)]

for i in range(n):
    s[i] = list(map(int, input().split()))

case = list(itertools.combinations(range(n), n//2))
k = len(case)
result = []

for i in range(k//2):
    start_sum = 0
    link_sum = 0
    for start in list(itertools.combinations(case[i], 2)):
        start_sum += s[start[0]][start[1]] + s[start[1]][start[0]]
    for link in list(itertools.combinations(case[-(i+1)], 2)):
        link_sum += s[link[0]][link[1]] + s[link[1]][link[0]]
    result.append(abs(start_sum - link_sum))

print(min(result))

백트래킹으로 풀어보자 !
"""

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = sys.maxsize

# a는 반까지 제어
def dfs(a, index):
    global result
    
    if a == n//2:
        start_sum = 0
        link_sum = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_sum += s[i][j]
                elif not visited[i] and not visited[j]:
                    link_sum += s[i][j]
        
        result = min(result, abs(start_sum - link_sum))
        return
    
    else:
        for i in range(index, n):
            if not visited[i]:
                visited[i] = True
                dfs(a+1, i+1)
                visited[i] = False
        
dfs(0, 0)
print(result)