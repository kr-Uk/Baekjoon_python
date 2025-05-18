t = int(input())
MSG_FORMAT = '#{} {}'

for test_case in range(1, t+1):
    n = int(input())
    money = list(map(int, input().split()))
    cnt = 0
    result = 0
    maximum = max(money)
    for i in range(n-1):
        if money[i] == maximum:
            result += cnt * money[i]
            cnt = 0
            maximum = max(money[i+1:])
        else:
            result -= money[i]
            cnt += 1
    result += cnt * money[-1]
    
    print(MSG_FORMAT.format(test_case, result))