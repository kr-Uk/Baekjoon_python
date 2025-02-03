"""
8*8씩 계속 잘라서 수정해야 하는 개수의 최솟값 구하기
맨 위 정사각형이 흰 또는 검 경우 나누기
인덱싱만 잘하면 될듯
"""

n, m = map(int, input().split())
chessBoard = []
min = 2500
white_chessBoard = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
black_chessBoard = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

for i in range(n):
    tmp = input()
    ilist = []
    for j in tmp:
        ilist.append(j)
    chessBoard.append(ilist)

for i in range(0, len(chessBoard)-7):
    for j in range(0, len(chessBoard[0])-7):
        white_cnt = 0
        black_cnt = 0
        cnt = 0
        for k in range(8):
            for m in range(8):
                if chessBoard[i+k][j+m] != white_chessBoard[k][m]:
                    white_cnt += 1
                if chessBoard[i+k][j+m] != black_chessBoard[k][m]:
                    black_cnt += 1
        if white_cnt >= black_cnt:
            cnt = black_cnt 
        else:
            cnt = white_cnt
        if min > cnt:
            min = cnt
            
print(min)