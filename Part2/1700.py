import sys
input = sys.stdin.readline

n, k = map(int, input().split())
if n >= k:
    print(0)
    exit(0)
plug = list(map(int, input().split()))
multitap = set()
idx = 0
result = 0


for i in range(k):
    if len(multitap) == n:
        if plug[i] not in multitap:
            idx = i
            break
    multitap.add(plug[i])

for i in range(idx, k):
    if plug[i] in multitap:
        continue
        
    optimal = set()
    for j in range(i, k):
        if plug[j] in multitap:
            optimal.add(plug[j])
            
        if len(optimal) == n-1 or j == k-1:
            tmp = list(multitap - optimal)
            multitap.remove(tmp[0])
            multitap.add(plug[i])
            result += 1
            break

print(result)