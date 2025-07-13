MSG_FORMAT = '#{} {}'

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = -1e9
    
    idx = 0
    
    for i in range(abs(n-m)+1):
        tmp = 0
        if n >= m:
            for j in range(m):
                tmp += a[j+idx] * b[j]
        else:
            for j in range(n):
                tmp += a[j] * b[j+idx]
        idx += 1
        result = max(result, tmp)
    print(MSG_FORMAT.format(test_case, result))