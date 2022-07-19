def solution(id_list, report, k):
    answer = [0] * len(id_list)         # 정답 리스트
    report = list(set(report))          # 중복 제거
    re_id = {i : 0 for i in id_list}    # 신고id 카운트

    # 신고 당한 횟수 카운트
    for re in report:
        re_id[re.split()[1]] += 1

    # k번 이상 신고당한 id를 신고한 이용자 메일 발송 카운트
    for re in report:
        if re_id[re.split()[1]] >= k:
            answer[id_list.index(re.split()[0])] += 1
    
    return answer