"""
그냥 sort로 하니까 길이를 따지지 않음.
c++이면 정렬 함수를 입맛대로 바꿀 수 있는데,, 파이썬도 있나?
=> key값 사용
근데 길이 별로 정렬하고, 알파벳 순으로 정렬도 해야 해
=> lambda
중복도 제거해야 돼
"""

n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())

word_list = list(set(word_list))
word_list.sort(key = lambda x:(len(x), x))

for w in word_list:
    print(w)