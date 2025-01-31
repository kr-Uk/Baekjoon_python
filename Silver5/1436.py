"""
666이 적어도 3개
3자리수 1개
4자리수 1, 2, 3, ... + '666' 그 다음 반대
5자리수 10, 11, 12, ...
...

특별한 규칙을 찾지 못함
=> 브루트 포스
"""

n = int(input())
cnt = 0
number = 665

while True:
    number += 1
    if '666' in str(number):
        cnt += 1
    if cnt == n:
        break
    
print(number)