import sys
input = sys.stdin.readline

a = list(input().strip())
stack = []
isCal = True
result = 0

for s in a:
    if s == '(':
        stack.append(2)
        isCal = False
    elif s == ')':
        if stack:
            if stack[-1] == 2:
                if not isCal:
                    tmp = 1
                    for i in stack:
                        tmp *= i
                    result += tmp 
                stack.pop()
                isCal = True
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)
    elif s == '[':
        stack.append(3)
        isCal = False
    elif s == ']':
        if stack:
            if stack[-1] == 3:
                if not isCal:
                    tmp = 1
                    for i in stack:
                        tmp *= i
                    result += tmp 
                stack.pop()
                isCal = True
            else:
                print(0)
                exit(0)
        else:
            print(0)
            exit(0)
    else:
        print(0)
        exit(0)

if stack:
    print(0)
else:
    print(result)