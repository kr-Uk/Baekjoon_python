nanjang = [0] * 9

for i in range(9):
    nanjang[i] = int(input())

result = sum(nanjang)
find_two = result - 100
a, b = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if nanjang[i] + nanjang[j] == find_two:
            a, b = nanjang[i], nanjang[j]
            break

nanjang.remove(a)
nanjang.remove(b)
nanjang.sort()

for i in range(7):
    print(nanjang[i])