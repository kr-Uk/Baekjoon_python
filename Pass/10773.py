n = int(input())
zero = []

for i in range(n):
    tmp = int(input())
    if tmp == 0 and zero:
        zero.pop()
    else:
        zero.append(tmp)

print(sum(zero))