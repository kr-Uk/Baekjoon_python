n = int(input())
cnt_5 = n // 5
while True:
    if cnt_5 == -1:
        print(-1)
        exit(0)
        
    if (n - (cnt_5 * 5)) % 3 == 0:
        break
    else:
        cnt_5 -= 1
        
print(cnt_5 + (n - (cnt_5 * 5)) // 3)
        