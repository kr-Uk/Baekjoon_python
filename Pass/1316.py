"""
그냥 셋 만들면 될듯?
"""

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    word = list(input())
    isChecker = True
    checked = set([])
    for i in range(len(word)-1):
        if word[i] in checked:
            isChecker = False
            break
        if word[i] == word[i+1]:
            continue
        elif word[i] != word[i+1]:
            checked.add(word[i])
    
    if isChecker:
        cnt += 1

print(cnt)