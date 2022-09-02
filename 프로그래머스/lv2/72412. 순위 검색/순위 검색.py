def solution(info, query):
    import bisect   # 이진 탐색

    answer = []     # 정답 저장

    info_dic = {}   # 문의조건 리스트

    # 문의조건 리스트 생성
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for menu in ['chicken', 'pizza', '-']:
                    info_dic[lang + job + career + menu] = []
    # 지원자의 점수를 문의조건 리스트에 추가
    for i in info:
        i = i.split(' ')
        for lang in [i[0], '-']:
            for job in [i[1], '-']:
                for career in [i[2], '-']:
                    for menu in [i[3], '-']:
                        info_dic[lang + job + career + menu].append(int(i[4]))
    # 점수를 기준으로 정렬
    for i_d in info_dic:
        info_dic[i_d].sort()
    # 문의조건만큼 반복
    for q in query:
        # ' and '를 제거해서 이어 붙인다.
        requir = q.replace(' and ', '').split()
        # 점수
        score = int(requir[1])
        # 조건
        requir = requir[0]
        # 조건을 키로 문의한 점수 이상의 지원자 수
        result = len(info_dic[requir]) - bisect.bisect_left(info_dic[requir], score)

        answer.append(result)

    return answer