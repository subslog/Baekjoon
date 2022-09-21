from itertools import combinations_with_replacement
def score_cal(apeach: list, ryan: list):
    """어피치와 라이언의 점수 차이를 계산하는 함수"""
    # 어피치, 라이언 점수
    a_score = 0
    r_score = 0
    for i in range(1, 11):
        # 둘 중 한 명이라도 과녁을 맞췄으면 계산
        if apeach[i] or ryan[i]:
            # 어피치 점수 획득
            if apeach[i] >= ryan[i]:
                a_score += i
            # 라이언 점수 획득
            else:
                r_score += i
    # 점수 차이 반환
    return r_score - a_score

def target_check(existing: list, now: list):
    """두 가지 경우 중 더 적은 과녁을 맞춘 경우를 반환"""
    e_cnt = 0
    n_cnt = 0
    for i in range(11):
        e_cnt += i * existing[i]
        n_cnt += i * now[i]
    if e_cnt < n_cnt:
        return existing
    else:
        return now

def solution(n, info):
    answer = [-1]
    # 점수를 뒤집는다
    info.reverse()
    # 라이언이 과녁을 맞추는 모든 경우의 수
    combi = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
    # 라이언의 모든 경우의 수와 비교하여 최대 점수 차이를 찾는다.
    max_diff = 0
    for c in combi:
        # 라이언이 맞춘 과녁
        ryan = [0] * 11
        for i in c:
            ryan[i] += 1
        # 현재 점수 차이
        now_diff = score_cal(info, ryan)
        # 라이언의 점수가 더 높으면 점수 갱신
        if max_diff < now_diff:
            max_diff = now_diff
            answer = ryan
    # 점수를 뒤집는다.
    answer.reverse()

    return  answer