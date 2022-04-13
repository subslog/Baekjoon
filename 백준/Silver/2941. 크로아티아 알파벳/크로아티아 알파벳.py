croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

sum = 0     # 크로아티아 알파벳 수

# 변경 알파벳 검사
for i in croatia:
    # 변경 알파벳 수만큼 증가
    sum += word.count(i)
    # 변경 알파벳을 *로 치환
    word = word.replace(i, '*')

# *을 제거
word = word.replace('*', '')
# 남은 알파벳 수만큼 증가
sum += len(word)

print(sum)