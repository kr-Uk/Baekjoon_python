MSG_FORMAT = '#{}'
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    angle_0 = [list(input().split()) for _ in range(n)]
    angle_90 = [[] for _ in range(n)]
    angle_180 = [[] for _ in range(n)]
    angle_270 = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n-1, -1,-1):
            angle_90[i].append(angle_0[j][i])
    
    for i in range(n):
        for j in range(n-1, -1,-1):
            angle_180[i].append(angle_90[j][i])
            
    for i in range(n):
        for j in range(n-1, -1,-1):
            angle_270[i].append(angle_180[j][i])
            
    print(MSG_FORMAT.format(test_case))
    
    for i in range(n):
        a = ''
        b = ''
        c = ''
        for j in range(n):
            a += angle_90[i][j]
            b += angle_180[i][j]
            c += angle_270[i][j]
        
        print(a, b, c)