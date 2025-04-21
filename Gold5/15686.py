"""
bfs로 탐색
상하좌우 +1씩

1을 시작으로 상하좌우 확인하고, 미리 m개만큼 2를 뽑아야 할 듯..?
아닌거같아,, 너무 오래걸려
2를 만날 때마다 ++ 시켜서 제일 큰 거 m개만큼..?
이것도 아니야.. 바로 옆에 있기만하면 다 +1씩인데..
경우의 수 맞는 것 같은디..?
백트래킹..!
경우의 수 다 찾기
사실 조합 사용하면 편하긴 함..!
"""

import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
