"""
일단 친절하게 재귀라고 나와있다.
n = 3
***
* *
***
n = 9
result ['*********', '* ** ** *', '*********'
        '***   ***', '* *   * *', '***   ***'
        '*********', '* ** ** *', '*********']
"""

def draw_star(n):
    if n == 1:
        return '*'
    
    stars = draw_star(n//3)
    result = []
    
    for S in stars:
        result.append(S*3)
    for S in stars:
        result.append(S+' '*(n//3)+S)
    for S in stars:
        result.append(S*3)
    
    return result

ans = draw_star(int(input()))
for a in ans:
    print(a)