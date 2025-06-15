"""
import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
pi = [0] * len(p)
pi[0] = 0

for i in range(1, len(p)):
    tmp = p[:i+1]
    for j in range((i+1)//2):
        if tmp[:j+1] == tmp[-(j+1):]:
            pi[i] = j+1

idx = 0

while idx <= len(s) - len(p):
    cnt = -1
    for i in range(len(p)):
        if s[idx+i] == p[i]:
            cnt += 1
        else:
            break
        
    if cnt == len(p)-1:
        print(1)
        exit(0)
    if cnt > 0 and pi[cnt] > 0:
        idx += len(p) - pi[cnt]
    else:
        idx += 1
        
print(0)
"""

import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

def make_table(p):
    table = [0] * len(p)
    
    j = 0
    for i in range(1, len(table)):
        while j > 0 and p[i] != p[j]:
            j = table[j-1]
        
        if p[i] == p[j]:
            j += 1
            table[i] = j
    
    return table

def kmp(s, p, table):
    i, j = 0, 0
    
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
            
        if s[i] == p[j]:
            j += 1
            if j == len(p):
                return True
    
    return False

table = make_table(p)
print([0, 1][kmp(s, p, table)])
