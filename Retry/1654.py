k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

end = max(lan)
start = 1

while end >= start:
    cnt = 0
    mid = (start + end) // 2
    for i in lan:
        cnt += i // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)