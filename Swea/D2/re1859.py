MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    result = 0
    cnt = 0
    n = int(input())
    ilst = list(map(int, input().split()))
    max_profit = max(ilst)
    for i in range(n):
        if ilst[i] == max_profit:
            result += max_profit * cnt
            if i != n-1:
                max_profit = max(ilst[i+1:])
                cnt = 0
        else:
            result -= ilst[i]
            cnt += 1
            
    print(MSG_FORMAT.format(test_case, result))