MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    if n == m:
        print(MSG_FORMAT.format(test_case, '='))
    elif n > m:
        print(MSG_FORMAT.format(test_case, '>'))
    else:
        print(MSG_FORMAT.format(test_case, '<'))