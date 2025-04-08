"""
시간초과 ! 처음 생각한 방법

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
"""

import sys
import itertools
input = sys.stdin.readline
maximum = -1e9
minimum = 1e9

n = int(input())
seq = list(map(int, input().split()))
op_num = list(map(int, input().split()))

def dfs(k, temp):
    global maximum, minimum
    
    # 종료 조건
    if k == n-1:
        maximum = max(temp, maximum)
        minimum = min(temp, minimum)
        return
    
    if op_num[0] != 0:
        op_num[0] -= 1
        dfs(k+1, temp + seq[k+1])
        op_num[0] += 1
    
    if op_num[1] != 0:
        op_num[1] -= 1
        dfs(k+1, temp - seq[k+1])
        op_num[1] += 1
        
    if op_num[2] != 0:
        op_num[2] -= 1
        dfs(k+1, temp * seq[k+1])
        op_num[2] += 1
    
    if op_num[3] != 0:
        op_num[3] -= 1
        dfs(k+1, int(temp / seq[k+1]))
        op_num[3] += 1

dfs(0, seq[0])

print(maximum)
print(minimum)