"""
이것도 이진탐색으로 해야할 듯..?
1 ~ min
이러면
4 4
10
1000
1000
1000
이런게 답이 10이 나오네
1~max로 !
"""

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in lan:
        sum += i // mid 
    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)