def passwd(idx: int, start: int):
    """암호를 출력하는 함수"""
    # L자리 패스워드가 되면 출력 후 재귀 종료
    if idx == L:
        # 모음, 자음 카운트
        cnt1 = cnt2 = 0
        for i in pwd:
            # 모음이 있으면 cnt1 증가, 아니면 cnt2 증가
            if i in ["a", "e", "i", "o", "u"]:
                cnt1 += 1
            else:
                cnt2 += 1
        # 모음 1개, 자음 2개 이상이면 출력
        if cnt1 >= 1 and cnt2 >= 2:
            print("".join(pwd))
        return

    for i in range(start, C):
        pwd[idx] = alpha[i]     # 패스워드 저장
        passwd(idx + 1, i + 1)  # 다음 패스워드 저장

L, C = map(int, input().split())
alpha = sorted(input().split()) # 오름차순으로 정렬 후 저장
pwd = [0] * L                   # 패스워드
passwd(0, 0)