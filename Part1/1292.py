n = 10
ilst = []
while n * (n+1) < 2000:
    n += 1

for i in range(1, n+1):
    for j in range(i):
        ilst.append(i)

start, end = map(int, input().split())

print(sum(ilst[start-1:end]))