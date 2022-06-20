S = input()

alp_dic = {}    # 알파벳 개수 저장 딕셔너리

# 딕셔너리 생성
for alp in range(97, 123):
    alp_dic[alp] = 0
# 알파벳 카운트
for s in S:
    alp_dic[ord(s)] += 1

print(*list(alp_dic.values()))