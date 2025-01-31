n = input()

num_list = []

for i in n:
    num_list.append(int(i))

num_list.sort()

x = 0
number = 0

for i in num_list:
    number += i * 10**x
    x += 1
    
print(number)