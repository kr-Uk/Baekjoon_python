"""
일단 다 탐색하긴 해야 돼
1 4 / q = [[1, 4]]
3 5 / x
0 6 / x
5 7 / q = [[1, 4], [5, 7]]
3 8 / x
5 9 / x
...
8 11 / q = [[1, 4], [5, 7], [8, 11]]
...
12 14 / q = [[1, 4], [5, 7], [8, 11], [12, 14]]

시간초과...

운영체제에서 스케줄링이랑 비슷하다는 생각
1. 회의가 일찍 끝나는 순 정렬 후 채택
2. 끝나는 시간을 기준으로 시작시간 필터링
3. 1, 2 반복
내가 간과한 것...
그냥 끝나는시간 정렬하고 시작시간 조건에만 맞으면 계속 채택임...
그 뒤에 것을 신경쓸 필요가 없었다..
"""

import sys
input = sys.stdin.readline

n = int(input())
cour = [list(map(int, input().split())) for _ in range(n)]
cour.sort(key = lambda x : (x[1], x[0]))
end = 0
result = 0

for new_start, new_end in cour:
    if new_start >= end:
        result += 1
        end = new_end

print(result)