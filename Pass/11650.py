import sys
input = sys.stdin.readline

n = int(input())
coor = []
for _ in range(n):
    coor.append(list(map(int, input().split())))

coor.sort()

for x, y in coor:
    print(x, y)