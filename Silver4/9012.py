"""
일단 개수는 같아야 함. (: -1 ): +1 해서 0
근데 음수로 갈 수는 없음.
"""

n = int(input())
is_vps = []

for _ in range(n):
    vps = input()
    cnt_ps = 0
    for s in vps:
        if cnt_ps < 0:
            break
        else:
            if s == '(':
                cnt_ps += 1
            else:
                cnt_ps -= 1
    if cnt_ps == 0:
        is_vps.append("YES")
    else:
        is_vps.append("NO")
        
for s in is_vps:
    print(s)