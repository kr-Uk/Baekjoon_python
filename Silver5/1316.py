# 그룹 단어 체커

import sys

n = int(sys.stdin.readline())
count = n

for i in range(n):
    word = sys.stdin.readline()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break

print(count) 
