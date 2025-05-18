"""
각 행의 합 100개, 열의 합 100개, 대각선 합 2개
"""
msg_FORMAT = "#{} {}"
for c in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row_sum = [0] * 100
    col_sum = [0] * 100
    dia_sum = [0, 0]
    
    for i in range(100):
        for j in range(100):
            row_sum[i] += arr[j][i]
            col_sum[j] += arr[j][i]
    
    for i in range(100):
        dia_sum[0] += arr[i][i]
        dia_sum[1] += arr[i][99-i]
    
    print(msg_FORMAT.format(c, max(max(row_sum), max(col_sum), max(dia_sum))))