def solution(id_list, report, k):
    # 메일을 받을 신고한 ID 목록 및 신고 당한 ID
    reporter_id = dict()
    black_id = dict()
    for id in id_list:
        reporter_id[id] = 0
        black_id[id] = set()
    # 신고한 ID 추가
    for re in report:
        user_id = re.split()
        black_id[user_id[1]].add(user_id[0])
    # k회 이상 신고된 ID 확인
    for b_id in black_id:
        # k회 이상 신고되었으면 신고한 ID에 메일을 보낸다.
        if k <= len(black_id[b_id]):
            for email_id in black_id[b_id]:
                reporter_id[email_id] += 1
                
    return list(reporter_id.values())