"""
별찍기처럼 재귀를 쓰기
2차원 배열 만들고 값을 넣으려고 했는데...
2^15 * 2^15 말 안돼,,
사분면 나누기
7 - > 3
6 -> 2
5 -> 1
4 -> 0
"""

import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = 0

while N > 0:
    if 0 <= r < (2**N)//2 and 0 <= c < (2**N)//2:
        ans += 0
    elif 0 <= r < (2**N)//2 and (2**N)//2 <= c < 2**N:
        ans += 4**(N-1)
        c -= (2**N) // 2
    elif (2**N)//2 <= r < 2**N and 0 <= c < (2**N)//2:
        ans += 2 * (4**(N-1))
        r -= (2**N) // 2
    elif (2**N)//2 <= r < 2**N and (2**N)//2 <= c < 2**N:
        ans += 3 * (4**(N-1))
        r -= (2**N) // 2
        c -= (2**N) // 2
        
    N -= 1

print(ans)