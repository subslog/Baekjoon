def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}   # 각 점수를 계산할 보너스
    scores = []                     # 각 라운드 점수 저장
    score = ''
    
    round = -1
    # 다트 결과 반복
    for i in dartResult:
        # 숫자면 점수 추가
        if i.isdecimal():
            score += i
        # 알파벳이면
        elif i.isalpha():
            # 점수 추가 후 초기화
            scores.append(int(score))
            score = ''
            # 현재 라운드
            round += 1
            # 보너스 계산
            scores[round] **= bonus[i]
        # 스타상(*)
        elif i == '*':
            # 첫 번째 라운드가 아니면 이전 라운드 점수도 *2
            if round != 0: scores[round - 1] *= 2
            scores[round] *= 2
        # 아차상(#)
        elif i == '#':
            scores[round] *= -1
    
    answer = sum(scores)
    
    return answer