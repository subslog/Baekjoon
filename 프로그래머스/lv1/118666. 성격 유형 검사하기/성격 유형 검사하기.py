def solution(survey, choices):
    answer = ''
    # 성격 유형 리스트
    survey_list = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    # 성격 유형 점수
    survey_cnt = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # 선택지에 따른 점수
    score = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    # 선택지에 따라 성격 유형 카운트
    for i in range(len(survey)):
        # 1 ~ 3 번이면 첫 번째 성격 유형 증가
        if choices[i] <= 3:
            survey_cnt[survey[i][0]] += score[choices[i]]
        # 5 ~ 7 번이면 두 번째 성격 유형 증가
        elif 5 <= choices[i]:
            survey_cnt[survey[i][1]] += score[choices[i]]
    # 성격 유형 결과
    for s_l in survey_list:
        # 같으면 사전순으로 빠른 유형이 추가된다.
        answer += max(s_l, key=lambda x: survey_cnt[x])
    
    return answer