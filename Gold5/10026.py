"""
이건 bfs나 dfs사용하면 쉬울 듯한데?
색약인 경우에는 그냥 R로 다 바꿔서 하면 되자너
"""

import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
area = [list(input().strip()) for _ in range(n)]
rb_area = copy.deepcopy(area)
for i in range(n):
    for j in range(n):
        if rb_area[i][j] == 'G':
            rb_area[i][j] = 'R'
            
cnt = [0, 0]

def dfs(x, y, rgb):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == rgb:
            area[nx][ny] = 0
            dfs(nx, ny, rgb)

for i in range(n):
    for j in range(n):
        if area[i][j] != 0:
            rgb = area[i][j]
            cnt[0] += 1
            area[i][j] = 0
            dfs(i, j, rgb)

area = copy.deepcopy(rb_area)
for i in range(n):
    for j in range(n):
        if area[i][j] != 0:
            rgb = area[i][j]
            cnt[1] += 1
            area[i][j] = 0
            dfs(i, j, rgb)
            
print(cnt[0], cnt[1])