"""
K보다 큰 가치 제외
제일 큰 값부터 나누고 나머지 반복
"""

n, k = map(int, input().split())
value = []
cnt = 0

for _ in range(n):
    tmp = int(input())
    if tmp > k:
        break
    else:
        value.append(tmp)
        
while k != 0:
    cnt += k // value[-1]
    k = k % value[-1]
    value.pop(-1)

print(cnt)