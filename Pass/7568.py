"""
덩치
"""

n = int(input())
dungchi = []

for _ in range(n):
   dungchi.append(list(map(int, input().split()))) 

dungchi.sort(reverse=True)

print(dungchi)