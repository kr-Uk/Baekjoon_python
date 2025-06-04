"""
antic
words에는 뭐가 들어가냐ㅑ
rc, hello, car 인데 여기서 antic 뺸거
alpha에는 r, c, h, e, l, l, o, c, a, r에서 antic 뺸거
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

antic = set('antic')
compare_set = set()
words = []
alpha = []

for i in range(n):
    words.append(set(input().strip()[4:-4])-antic)

for w in words:
    alpha.extend(list(w))

alpha = list(set(alpha))

if k <= 4:
    print(0)
    exit(0)

cnt = k-5
result = 0

def dfs(c, idx):
    global result
    
    if c == cnt or c == len(alpha):
        tmp = 0
        for i in range(n):
            if words[i] <= compare_set:
                tmp += 1
        result = max(tmp, result)
        return
    
    for i in range(idx, len(alpha)):
        compare_set.add(alpha[i])
        dfs(c+1, i+1)
        compare_set.remove(alpha[i])

dfs(0, 0)
print(result)