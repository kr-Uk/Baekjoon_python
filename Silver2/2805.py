"""
내림차순으로 sort하고, 1씩 뺴면서 인덱스 값끼리 비교하기?

20 17 15 10이면
19 17 15 10 : 1
18 17 15 10 : 2
17 17 15 10 : 3
16 16 15 10 : 5
15 15 15 10 : 7

근데 문제는 시간초과..
10^6이 최대 길이니까 nlog(n)까지 가능해

아니면 그냥 첫 번째 원소 기준으로 잘라보면서 범위값으로 찾아보기?
그러면 잘랐을 때 차를 알아야 해

4 42 40 26 46
46 + 4 = 50
25가 기준
17 + 15 + 1 + 21 > 20
46 + 25 = 71
35가 기준
7 + 5 + 11 > 20
46 + 35 = 81
40이 기준
2 + 6 < 20
40 + 35 = 75
37이 기준
5 + 3 + 9 < 20
37 + 35 = 72
36이 기준
6 + 4 + 10 = 20
36 !

=> 시간 초과...

위 개념이 이분탐색 개념인데 구현을 잘 못한 것 같다..
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
min, max = 1, max(tree)

while min <= max:
    pivot = (min + max) // 2 # // (몫) !!
    sum = 0
    for i in tree:
        if i > pivot:
            sum += i-pivot
    
    if sum >= m:
        min = pivot + 1
    else:
        max = pivot - 1

print(max)