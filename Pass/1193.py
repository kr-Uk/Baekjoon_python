"""
분수찾기
"""

n = int(input())
compare = 0

while True:
    if compare * (compare + 1) / 2 == n:
        if compare % 2 == 0:
            print(str(compare) + '/' + '1')
        else:
            print('1' + '/' + str(compare))
        break
    if (compare + 1) * (compare + 2) / 2 > n and compare * (compare + 1) / 2 < n:
        tmp = n - (compare * (compare + 1) // 2)
        x = compare + 2
        y = 0
        for _ in range(tmp):
            x -= 1
            y += 1
        if compare % 2 == 1:
            print(str(y) + '/' + str(x))
        else:
            print(str(x) + '/' + str(y))
        break
    compare += 1