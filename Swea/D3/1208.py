msg_FORMAT = '#{} {}'

for t in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    for i in range(n):
        maximum = max(box)
        minimum = min(box)
        box[box.index(maximum)] -= 1
        box[box.index(minimum)] += 1
    print(msg_FORMAT.format(t, max(box) - min(box)))