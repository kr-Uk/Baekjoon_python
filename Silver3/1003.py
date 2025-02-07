"""
DP 점화식 찾기

fib[0] = 1 0
fib[1] = 0 1
fib[2] = 1 1
fib[3] = 1 2
fib[4] = fib[3] + fib[2] = 2 3
fib[5] = fib[4] + fib[3] = 3 5
...
fib[n] = fib[n-1] + fib[n-2]
"""

fib = [0] * 41
fib[0] = [1, 0]
fib[1] = [0, 1]

for i in range(2, 41):
    fib[i] = [fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1]]

t = int(input())

for _ in range(t):
    print(*fib[int(input())])
