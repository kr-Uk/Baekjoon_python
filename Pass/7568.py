"""
덩치
"""

n = int(input())
dungchi = []
rank = [1] * n

for _ in range(n):
   dungchi.append(list(map(int, input().split()))) 

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end=" ")