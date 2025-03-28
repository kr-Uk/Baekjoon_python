"""
1, 2, 3, 4, 5, 6, 7, 8
seq = [3, 4]
stack = [3, 4]
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

result = []
seq = deque([])
for _ in range(n):
    seq.append(int(input()))

stack = []
for i in range(1, n+1):
   stack.append(i)
   result.append('+')
   while stack[-1] == seq[0]:
       stack.pop()
       result.append('-')
       seq.popleft()
       if not stack:
           break

if seq:
    print('NO')
else:
    for i in result:
        print(i)