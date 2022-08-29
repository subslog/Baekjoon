def combi(index: int, k: int, mask: int):
    """k개의 배울 수 있는 단어 조합을 만드는 함수"""
    # 종료 조건 : k 개의 알파벳을 모두 선택
    if k == 0:
        word_combi.append(mask)
        return
    # 종료 조건 : a, c, i, n, t가 포함되지 않으면 정답 0
    elif k < 0:
        return
    # 종료 조건 : z까지 모두 확인했으면 종료
    if index == 21:
        return
    # 알파벳을 선택
    combi(index + 1, k - 1, mask | (1 << alpha[index]))
    # 알파벳을 선택하지 않음
    combi(index + 1, k, mask)

# 초기 입력값
N, K = map(int,input().split())
K -= 5
words = [0] * N
# i 번째 단어를 비트 마스크로 저장 : a:0 ~ z:25
for i in range(N):
    word = input()
    for w in word:
        words[i] |= 1 << (ord(w) - 97)
# a, c, n, i, t는 필수 알파벳이므로 비트 마스크에 추가
alpha = []
mask = 0
for i in range(26):
    if i in [0, 2, 8, 13, 19]:
        mask |= 1 << i
    else:
        alpha.append(i)
# k 개의 알파벳을 배울 수 있는 조합 생성
word_combi = []
combi(0, K, mask)
# 읽을 수 있는 단어 개수의 최대값
ans = 0
for w_c in word_combi:
    cnt = 0
    for word in words:
        # 입력된 단어와 배우지 않은 단어의 and 연산 결과가 0이면 배우지 않은 단어가 없다.
        if word & ((1 << 26) - 1 - w_c) == 0:
            cnt += 1
    ans = max(ans, cnt)

print(ans)