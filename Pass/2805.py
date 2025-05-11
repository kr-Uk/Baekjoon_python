import sys
input = sys.stdin.readline

n, m = map(int, input().split())
namu = list(map(int, input().split()))

start = 1
end = max(namu)

while start <= end:
    mid = (start + end) // 2
    tmp = list(filter(lambda x: x > mid, namu))
    length = sum(tmp) - (len(tmp) * mid)
    
    if length >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)