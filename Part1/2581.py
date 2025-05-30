m = int(input())
n = int(input())
primeN = []

for i in range(m, n+1):
    if i <= 1:
        continue
    isPrime = True
    for j in range(2, int(i ** (0.5))+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primeN.append(i)

if primeN:
    print(sum(primeN))
    print(primeN[0])
else:
    print(-1)
    
