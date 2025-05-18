"""
?를 만날 때마다 L또는 R로 대체 후 결과 확인
근데 그냥 다 확인하면 안되나..? 반복문으로
조합 사용해서 채워넣기?

from itertools import combinations_with_replacement
msg_FORMAT = '{}'
n = int(input())

for c in range(1, n+1):
    graph = list(input())
    cnt = 0
    for g in graph:
        if g == '?':
            cnt += 1
    
    for i in combinations_with_replacement(['L', 'R'], cnt):
        tmp = [0] * (len(graph)+1)
        idx = 0
        result = -10000
        for j in range(len(graph)):
            if graph[j] == '?':
                if i[idx] == 'L':
                    tmp[j+1] = tmp[j] - 1
                else:
                    tmp[j+1] = tmp[j] + 1
                idx += 1
            else:
                if graph[j] == 'L':
                    tmp[j+1] = tmp[j] - 1
                else:
                    tmp[j+1] = tmp[j] + 1
        result = max(result, abs(max(tmp)), abs(min(tmp)))
        
    print(msg_FORMAT.format(result))
    
이게 틀림

완전탐색해야할듯? backtracking !

t = int(input())

def dfs(n, cnt):
    global result
    result = max(result, abs(cnt))
    if n == len(test_case):
        return
    
    if test_case[n] == 'L':
        dfs(n+1, cnt-1)
    elif test_case[n] == 'R':
        dfs(n+1, cnt+1)
    else:
        dfs(n+1, cnt-1)
        dfs(n+1, cnt+1)

for _ in range(t):
    test_case = list(map(str, input()))
    result = 0
    dfs(0, 0)
    print(result)

이게 시간초과

근데 무조건 극단적인게 좋지 않나?
다 L로 바꾸거나 다 R로 바꾸기
맞네...
"""

t = int(input())


for _ in range(t):
    test_case = list(map(str, input()))
    result = 0
    all_L = 0
    all_R = 0
    for i in test_case:
        if i == 'L':
            all_L -= 1
            all_R -= 1
        elif i == 'R':
            all_L += 1
            all_R += 1
        else:
            all_L -= 1
            all_R += 1
        result = max(result, abs(all_L), abs(all_R))
    
    print(result)