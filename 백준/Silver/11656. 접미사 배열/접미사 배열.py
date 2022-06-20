S = input()

answer = []   # 정답 저장 리스트

# 문자열 왼쪽에서 1개씩 제거하면서 answer에 추가
for i in range(len(S)):
    answer.append(S[i:len(S)])

# 오름차순 정렬
print("\n".join(sorted(answer)))