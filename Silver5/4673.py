"""
입력값 X
10000보다 작거나 같은 생성자가 있는 숫자를 제거
1~10000까지의 집합 - 생성자 집합    
"""

num = set(range(1, 10001))
remove_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if i <= 10000:
        remove_set.add(i)
        
self_number = num - remove_set
            
for i in sorted(self_number):
    print(i)