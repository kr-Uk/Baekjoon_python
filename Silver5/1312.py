"""
나눗셈 연산대로 하면 되지 않나?
25 7 5 를 예시로
25 // 7 = 3
25 % 7 = 4
4 * 10 = 40
40 % 7 = 5 
5 * 10 = 50
50 % 7 = 1
...
"""

a, b, n = map(int, input().split())

for _ in range(n+1):
    tmp = a // b
    a = (a % b) * 10
    
print(tmp)