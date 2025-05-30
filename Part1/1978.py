n = int(input())
primeN = list(map(int, input().split()))
cnt = 0

for i in range(n):
    isPrime = True
    d = 2
    if primeN[i] <= 1:
        continue
    while primeN[i] > d:
        if primeN[i] % d == 0:
            isPrime = False
            break
        d += 1
    if isPrime:
        cnt += 1
        
print(cnt)