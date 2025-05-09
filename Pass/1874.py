n = int(input())
seq = []
stack = []
result = []
idx, cnt_plus, cnt_minus = 0, 0, 0
for _ in range(n):
    seq.append(int(input()))
    
for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    cnt_plus += 1
    while stack and stack[-1] == seq[idx]:
        stack.pop()
        result.append('-')
        cnt_minus += 1
        idx += 1

if cnt_plus == cnt_minus:
    for r in result:
        print(r)
else:
    print('NO')
    