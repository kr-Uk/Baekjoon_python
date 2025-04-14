"""
하노이탑!
recursion을 이용했던 것 같은데
7
23 0 1
3 2 1
3 21 0 여기서 21을 보면 재귀
0 21 3 원판을 옮기고 2에서 3으로 1을 경유
"""

import sys
input = sys.stdin.readline

n = int(input())
print(2**n - 1) # hanoi(n) = hanoi(n-1) * 2 + 1

def move(n, start, to):
    print(start, to)

def hanoi(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n-1, via, to, start)
        
hanoi(n, 1, 3, 2)