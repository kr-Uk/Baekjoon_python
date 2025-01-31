"""
규칙찾기
a1 = 1/1
a2 = 1/2
a3 = 2/1
a4 = 3/1
a5 = 2/2
a6 = 1/3
a7 = 1/4
...
n(n+1)/2 < k < (n+1)(n+2)/2 인 n값을 찾기
n+1 값이 홀수 -> 분자가 n+1부터 내림차순, 분모가 1부터 오름차순
n+1 값이 짝수 -> 반대
k-n(n+1)/2
"""

k = int(input())
n = 1

while not(n*(n+1)/2 <= k and k < (n+1)*(n+2)/2):
    n += 1
    
k = k - n*(n+1)//2

if (n+1) % 2 == 0:
    if k == 0:
        print(str(1) + '/' + str(n))
    else:
        print(str(k) + '/' + str(n-k+2))
else:
    if k == 0:
        print(str(n) + '/' + str(1))
    else:
        print(str(n-k+2) + '/' + str(k))