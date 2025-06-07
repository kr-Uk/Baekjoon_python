import sys
input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))
result = 1e9
ssum = 0
left, right = 0, 0

while True:
    """
    ssum += seq[right]
    right += 1
    
    while ssum >= s:
        ssum -= seq[left]
        left += 1
        result = min(result, right-left+1)
    
    if right == n:
        if result == 1e9:
            print(0)
        else:
            print(result)
        exit(0)
    """
    if ssum >= s:
        result = min(result, right-left)
        ssum -= seq[left]
        left += 1
    elif right == n:
        break
    else:
        ssum += seq[right]
        right += 1
        
if result == 1e9:
    print(0)
else:
    print(result)