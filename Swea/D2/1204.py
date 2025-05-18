MSG_FORMAT = '#{} {}'
t = int(input())

for _ in range(t):
    n = int(input())
    score = [0] * 101
    for s in list(map(int, input().split())):
        score[s] += 1
    result = []
    tmp = max(score)
    for i in range(101):
        if score[i] == tmp:
            result.append(i)
    
    print(MSG_FORMAT.format(n, max(result)))