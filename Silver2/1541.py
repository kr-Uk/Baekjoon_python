"""
일단 표기식이 나오면 스택부터 생각나긴해.
아니면 중위순회 트리?
- 기준
10 + 40 - (50 + 10) - 20 - 30
10+40 - 50+10 - 20 - 30
"""

import sys
input = sys.stdin.readline

exp = list(input().split('-'))
result = 0

for i in range(len(exp)):
    temp = map(int, exp[i].split('+'))
    sum = 0
    for j in temp:
        sum += j
    if i == 0:
        result += sum
    else:
        result -= sum

print(result)