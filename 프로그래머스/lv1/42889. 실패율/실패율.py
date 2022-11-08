def solution(N, stages):
    # 각 스테이지를 도달 및 도전 중인 사용자 수
    arrival_cnt = [0] * (N + 2)
    stages_cnt = [0] * (N + 2)
    for stage in stages:
        stages_cnt[stage] += 1
        # 현재 도전 중인 스테이지 이하는 모두 도달
        for round in range(1, stage + 1):
            arrival_cnt[round] += 1
    # 실패율 계산
    stages_failure = {i:0 for i in range(1, N + 1)}
    for i in range(1, N + 1):
        # 도달한 사용자가 있는 스테이지만 계산
        if 0 < arrival_cnt[i]:
            stages_failure[i] = stages_cnt[i] / arrival_cnt[i]
    # 실패율 오름차순 정렬해 스테이지 저장
    answer = sorted(stages_failure, key=lambda x: stages_failure[x], reverse=True)

    return answer