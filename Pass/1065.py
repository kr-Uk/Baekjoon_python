n = int(input())

if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n+1):
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            cnt += 1
    print(cnt)