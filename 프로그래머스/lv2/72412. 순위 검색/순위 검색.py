import bisect

def solution(info, query):
    answer = []
    # 쿼리 조건을 딕셔너리로 생성
    info_dict = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_dict[lang + job + career + food] = []
    # 지원자 정보에 맞게 점수 추가
    for user in info:
        lang, job, career, food, score = user.split()
        for l in [lang, '-']:
            for j in [job, '-']:
                for c in [career, '-']:
                    for f in [food, '-']:
                        info_dict[l + j + c + f].append(int(score))
    # 점수를 기준으로 정렬
    for key in info_dict:
        info_dict[key].sort()
    # 요구사항에 만족하는 지원자 수 확인
    for q in query:
        # ' and ' 제거하고 연결한다.
        requir, score = q.replace(' and ', '').split()
        answer.append(len(info_dict[requir]) - bisect.bisect_left(info_dict[requir], int(score)))
    
    return answer