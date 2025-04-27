n = str(input())
arr = []

for i in n:
    arr.append(int(i))

arr.sort()

result = 0
mul = 1
for i in arr:
    result += mul * i
    mul *= 10

print(result)