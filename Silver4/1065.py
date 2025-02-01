"""
일단 두 자리 수까지는 다 한수
1000도 한수는 아니니까 제외
세 자리 수만 파악하면 돼
"""

n = int(input())
numbers = list(range(100, n+1))
cnt = 0

if n < 100:
    print(n)
else:
    for k in numbers:
        if int(str(k)[1]) - int(str(k)[0]) == int(str(k)[2]) - int(str(k)[1]):
            cnt += 1
    print(99 + cnt)
