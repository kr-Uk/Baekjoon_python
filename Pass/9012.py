n = int(input())
vps = []
for _ in range(n):
    vps.append(list(input().strip()))

for i in range(n):
    q = []
    is_vps = True
    for j in vps[i]:
        if j == '(':
            q.append('(')
        else:
            if not q:
                is_vps = False
                break
            else:
                q.pop()
    if q:
        is_vps = False
    if is_vps:
        print('YES')
    else:
        print('NO')