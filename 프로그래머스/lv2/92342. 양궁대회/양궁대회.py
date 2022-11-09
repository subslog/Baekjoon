from itertools import combinations_with_replacement

def result(apeach: list, ryan: list):
    """라이언과 어피치의 점수차를 반환하는 함수"""
    # 어피치, 라이언 점수
    a_score, r_score = 0, 0
    # 점수 계산
    for i in range(11):
        # 둘 다 못맞추면 점수 획득 불가
        if apeach[i] == 0 and ryan[i] == 0:
            continue
        # 라이언 점수 획득
        elif apeach[i] < ryan[i]:
            r_score += i
        # 어피치 점수 획득
        else:
            a_score += i
    return r_score - a_score

def solution(n, info):
    answer = []
    
    # 편의를 위해 뒤집는다.
    info.reverse()
    # 라이언이 n번으로 맞출 수 있는 모든 케이스
    ryan_cases = list(combinations_with_replacement(list(range(0, 11)), n))
    # 라이언과 어피치 가장 큰 점수 차
    max_score = 0
    
    # 모든 케이스를 비교
    for case in ryan_cases:
        # 라이언 과녁 결과
        ryan = [0] * 11
        for hit in case:
            ryan[hit] += 1
        # 라이언 점수 - 어피치 점수
        score = result(info, ryan)
        # 현재 점수 차가 더 크면 업데이트
        if max_score < score:
            max_score = score
            answer = ryan
    # 라이언이 이길 수 없으면 -1
    if max_score == 0:
        answer = [-1]
    # 이길 수 있으면 뒤집는다.
    else:
        answer.reverse()

    return answer