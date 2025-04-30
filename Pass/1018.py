import sys
input = sys.stdin.readline

m, n = map(int, input().split())
chess = []
result = sys.maxsize

for _ in range(m):
    chess.append(list(input().strip()))

for i in range(m-7):
    for j in range(n-7):
        cnt_B = 0
        cnt_W = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] == 'B':
                        cnt_W += 1
                    else:
                        cnt_B += 1
                else:
                    if chess[x][y] == 'B':
                        cnt_B += 1
                    else:
                        cnt_W += 1 
        result = min(result, cnt_B, cnt_W)

print(result)