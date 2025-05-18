"""
farm[3:-3]
farm[2:-2]
farm[1:-1]
farm[0:]
"""

msg_FORMAT = "#{} {}"
t = int(input())

for c in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    result = 0
    
    for i in range(n):
        if i == n//2:
            for value in farm[i]:
                result += value
        elif i < n//2:
            for value in farm[i][n//2-i:-(n//2-i)]:
                result += value
        elif i > n//2:
            for value in farm[i][i-n//2:-(i-n//2)]:
                result += value
    
    print(msg_FORMAT.format(c, result))