MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    tmp, n = input().split()
    n = int(n)
    money = list(map(int, tmp))
    print(money, n)