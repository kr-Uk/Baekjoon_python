# 배열에 크로아티아 알파벳 넣기
# 크로아티아 알파벳을 replace로 한 음절로 대체
# 음절 개수 출력

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for w in croatia_alphabet:
    word = word.replace(w, '*')
    
print(len(word))