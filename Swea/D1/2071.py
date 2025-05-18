MSG_FORMAT = '#{} {}'

t = int(input())

for c in range(1, t+1):
    nums = list(map(int, input().split()))
    result = round(sum(nums) / len(nums))
    
    print(MSG_FORMAT.format(c, result))