import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    tmp = list(map(int, input().split()))
    print(sorted(tmp, reverse=True)[2])