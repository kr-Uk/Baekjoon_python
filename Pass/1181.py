"""
단어정렬
이거는 lambda !
"""

import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    tmp = input()
    if tmp not in words:
        words.append(tmp)

words.sort(key = lambda x : (len(x), x))

for i in words:
    print(i, end = "")