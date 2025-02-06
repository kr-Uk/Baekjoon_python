"""
소수 판별
8의 경우 2 * 4 = 4 * 2와 같은 식으로 대칭
=> 특정한 숫자의 제곱근까지만 약수 여부 검증
=> O(N^(1/2))

에라토스테네스의 체
=> 대량의 소수를 한꺼번에 판별별
"""

m, n = map(int, input().split())

number = list(range(0, n+1))
number[0] = 0
number[1] = 0

for i in range(2, n+1):
    if i == 0: continue
    for j in range(i+i, n+1, i):
        number[j] = 0

for i in number:
    if i >= m:
        print(i)