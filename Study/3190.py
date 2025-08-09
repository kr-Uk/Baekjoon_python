import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
for _ in range(k):
    
