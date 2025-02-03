"""
스택으로 쉽게 구현
"""

k = int(input())
money = []
result = 0

for _ in range(k):
    tmp = int(input())
    if tmp == 0 and len(money) != 0:
        money.pop(-1)
    else:
        money.append(tmp)

for i in money:
    result += i

print(result)