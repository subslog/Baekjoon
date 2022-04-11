word = input().upper()

set_word = set(word)    # 중복 제거

# 알파벳과 알파벳 수 저장 후 수를 기준으로 정렬 (내림차순)
word_c = sorted([[i, word.count(i)] for i in set_word], key=lambda x: x[1], reverse=True)

# 알파벳의 수가 하나
# 또는 첫 번째 알파벳 수와 두 번째 알파벳 수가 다르면 가장 많이 사용된 알파벳 출력
if len(word_c) == 1 or word_c[0][1] != word_c[1][1]:
    print(word_c[0][0])
else:
    print('?')