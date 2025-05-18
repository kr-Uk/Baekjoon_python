t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    up = n-2
    down = 1
    left = n-2
    right = 0
    cnt = 0
    for i in range(n**2):
        if right == n-cnt and down == n-cnt and left < cnt and up == cnt:
            cnt += 1
            right = cnt
            left = n-cnt-2
            up = n-cnt-2
            down = cnt+1
        if right < n-cnt:
            snail[down-1][right] = i+1
            right += 1
        elif down < n-cnt:
            snail[down][right-1] = i+1
            down += 1
        elif left >= cnt:
            snail[down-1][left] = i+1
            left -= 1
        elif up > cnt:
            snail[up][left+1] = i+1
            up -= 1
            
    print('#'+str(test_case))
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()