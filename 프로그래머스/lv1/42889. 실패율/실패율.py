def solution(N, stages):
    # 정답 저장 리스트
    answer = []
    # 각 스테이지에 머물러 있는 플레이어 리스트
    stay = [0] * (N + 2)
    # 실패율 저장 리스트
    fail = []
    
    # fail 리스트 카운트
    for i in stages:
        stay[i] += 1
    
    # 실패율 계산
    for i in range(1, N + 1):
        # 현재 스테이지를 도달한 플레이어 수
        success = sum(stay[i:])
        # 0이면 도달한 플레이어가 없다.
        if success == 0:
            fail.append((i, 0))
        else:
            fail.append((i, stay[i] / success))
    
    # 실패율 기준으로 정렬
    for i in sorted(fail, reverse=True, key=lambda x: x[1]):
        answer.append(i[0])

    return answer