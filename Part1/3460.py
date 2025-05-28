t = int(input())

for _ in range(t):
    n = int(input())
    ilst = []
    while n != 1:
        ilst.append(n%2)
        n = n//2
    ilst.append(1)
    
    for i in range(len(ilst)):
        if ilst[i] == 1:
            print(i, end = " ")
    print()