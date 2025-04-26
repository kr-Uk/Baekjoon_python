"""
셀프넘버
"""

import sys
input = sys.stdin.readline

nums = set([i for i in range(1, 10001)])

for i in range(1, 10001):
    tmp = str(i)
    non_selfNumber = i
    for j in tmp:
        non_selfNumber += int(j)
    if non_selfNumber in nums:
        nums.remove(non_selfNumber)

nums = sorted(list(nums))

for i in nums:
    print(i)