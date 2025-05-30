maximum = -1e9
people = 0

for _ in range(10):
    off, on = map(int, input().split())
    people += on - off
    maximum = max(maximum, people)
    
print(maximum)