import sys
input = sys.stdin.readline

n = int(input())
result = 0
bombo = [list(input().rstrip()) for _ in range(n)]    

def bomboni():
    result = 0
    for i in range(n):
        cnt_row = 1
        cnt_col = 1
        for j in range(1, n):
            if bombo[i][j-1] == bombo[i][j]:
                cnt_row += 1
            else:
                cnt_row = 1
            
            if bombo[j-1][i] == bombo[j][i]:
                cnt_col += 1
            else:
                cnt_col = 1
        
            result = max(result, cnt_row, cnt_col)
    
    return result

sol = bomboni()

for i in range(n):
    for j in range(n-1):
        bombo[i][j], bombo[i][j+1] = bombo[i][j+1], bombo[i][j]
        sol = max(sol, bomboni())
        bombo[i][j+1], bombo[i][j] = bombo[i][j], bombo[i][j+1]
        
        bombo[j][i], bombo[j+1][i] = bombo[j+1][i], bombo[j][i]
        sol = max(sol, bomboni())
        bombo[j+1][i], bombo[j][i] = bombo[j][i], bombo[j+1][i]
        
print(sol)