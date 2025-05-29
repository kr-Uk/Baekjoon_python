import sys
input = sys.stdin.readline

n = int(input())
ilst = list(map(int, input().split()))
minimum = 1e9
maximum = -1e9

for i in ilst:
    if i > maximum:
        maximum = i
    
    if i < minimum:
        minimum = i
        
print(minimum, maximum)