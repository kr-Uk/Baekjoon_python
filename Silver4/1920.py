"""
그냥 in 사용하면 시간초과가 나올듯..?
리스트 말고 set으로 ! set은 해시 테이블로 구현되어 있기 때문!
"""

import sys

n = int(input())
numbers = set(map(int, sys.stdin.readline().split()))

k = int(input())
chk_list = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    if chk_list[i] in numbers:
        print(1)
    else:
        print(0)