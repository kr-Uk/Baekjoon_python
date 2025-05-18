import sys
input = sys.stdin.readline
MSG_FORMAT = '#{} {}'

t = int(input())

for c in range(1, t+1):
    nums = list(map(int, input().split()))
    result = 0
    for i in nums:
        if i % 2 == 1:
            result += i
    
    print(MSG_FORMAT.format(c, result))