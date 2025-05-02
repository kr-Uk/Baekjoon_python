n = int(input())
vps = []
for _ in range(n):
    vps.append(list(input().strip()))

for i in range(n):
    idx = 0
    q = []
    is_vps = True
    while idx < n:
        if vps[i][idx] == '(':
            q.append(vps[i][idx])
            idx += 1
        else:
            if not q:
                print('hi')
                is_vps = False
                break
            while q:
                if vps[i][idx] != ')':
                    idx = n
                    is_vps = False
                    break
                q.pop()
                idx += 1
    if is_vps:
        print('YES')
    else:
        print('NO')