import re

def solution(dartResult):
    # 보너스 제곱
    bonus = {'S':1, 'D':2, 'T':3}
    # 다트 결과를 3라운드로 분리
    round = re.findall('(1*[0-9])([SDT])([*#]*)', dartResult)
    # 각 라운드 점수
    score = [0, 0, 0, 0]

    # 다트 점수 계산
    for i in range(3):
        # 점수에 보너스 점수만큼 제곱
        score[i + 1] = int(round[i][0]) ** bonus[round[i][1]]
        # 옵션이 있으면 적용
        if round[i][2] == '*':
            score[i] *= 2
            score[i + 1] *= 2
        elif round[i][2] == '#':
            score[i + 1] *= -1

    return sum(score[1:])