n = input().split('-')
result = 0
first_num = 0
for i in range(1, len(n)):
    tmp = n[i].split('+')
    for i in tmp:
        result += int(i)

for i in n[0].split('+'):
    first_num += int(i)

result = first_num - result
print(result)