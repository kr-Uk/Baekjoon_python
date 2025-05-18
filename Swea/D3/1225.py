from collections import deque

for c in range(1, 11):
    n = int(input())
    secret = deque(map(int, input().split()))
    while secret[-1] != 0:
        for i in range(1, 6):
            tmp = secret.popleft()
            if tmp-i <= 0:
                secret.append(0)
                break
            secret.append(tmp-i)
    
    print('#'+str(c), end=" ")
    for s in secret:
        print(s, end=" ")
    print()
            
            