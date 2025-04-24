"""
*로 바꾸기
"""

chro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

tmp = str(input())

for i in chro:
    tmp = tmp.replace(i, '*')

print(len(tmp))