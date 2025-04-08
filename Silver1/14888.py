"""
최대 10개의 연산자
10! / 중복!
"""

import sys
import itertools
input = sys.stdin.readline
maximum = -1e9
minimum = 1e9

n = int(input())
seq = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for i in range(4):
    for j in range(op_num[i]):
        op.append(op_list[i])

for i in list(itertools.permutations(op, n-1)):
    result = seq[0]
    for j in range(1, n):
        if i[j-1] == '+':
            result += seq[j]
        elif i[j-1] == '-':
            result -= seq[j]
        elif i[j-1] == '*':
            result *= seq[j]
        else:
            result = int(result / seq[j])
    if result > maximum:
        maximum = result
    if result < minimum:
        minimum = result

print(maximum)
print(minimum)