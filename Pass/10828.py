"""
스택... 
"""

n = int(input())
stack = []

for i in range(n):
    tmp = input().split()
    if tmp[0] == 'push':
        stack.append(int(tmp[1]))
    elif tmp[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif tmp[0] == 'top':
        print(stack[-1])
