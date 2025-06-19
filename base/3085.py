import sys
input = sys.stdin.readline

n = int(input())
candy = []

for _ in range(n):
    candy.append(list(input().rstrip()))
    
print(candy)