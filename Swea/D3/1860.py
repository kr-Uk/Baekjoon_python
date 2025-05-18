"""
재밌겠다
배열 11111+1 칸짜리 만들고
붕어빵 다 넣고
오는 시간 정렬해서 - 계속 하기
이거 아닌듯..?
"""
msgFORMAT = "#{} {}"
t = int(input())

for c in range(1, t+1):
    N, M, K = map(int, input().split())
    comeON = list(map(int, input().split()))
    bungAbbang = [0] * 11112
    for i in range(M, len(bungAbbang), M):
        bungAbbang[i] = K
        K *= 2
    comeON.sort()
    minus = 0
    isPossible = True
    for i in range(N):
        minus += comeON[i]
        if sum(bungAbbang[:i]) >= minus:
            pass
        else:
            isPossible = False
            break
    
    if isPossible:
        print(msgFORMAT.format(c, 'Possible'))
    else:
        print(msgFORMAT.format(c, 'Impossible'))