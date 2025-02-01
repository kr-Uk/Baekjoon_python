"""
알고리즘 이름이 있는데 까먹었다,,
5를 최대한 많이, 3을 최대한 적게
하나씩 빼고, 하나씩 늘리면서
만약 정확히 맞출 수 없다면 -1
"""

n = int(input())
change = n
cnt_five = n // 5
cnt_three = 0

while True:
    if cnt_five == -1:
        print(-1)
        break
    else:
        change = n - (cnt_five * 5)
        cnt_three = change // 3
        change = change % 3
        if change == 0:
            print(cnt_five + cnt_three)
            break
        else:
            cnt_five -= 1
