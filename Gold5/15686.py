"""
bfs로 탐색
상하좌우 +1씩

1을 시작으로 상하좌우 확인하고, 미리 m개만큼 2를 뽑아야 할 듯..?
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

