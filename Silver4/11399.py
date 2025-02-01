"""
그냥 정렬해서 곱하기로 하면 될듯?
"""

n = int(input())
atm = list(map(int, input().split()))

atm.sort()

result = 0

for i in atm:
    result += i * n
    n -= 1
    
print(result)