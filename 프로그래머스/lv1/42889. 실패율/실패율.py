def solution(N, stages):
    # 정답 저장 리스트
    answer = []
    # 각 스테이지 도달한 플레이어 수
    arrival = [0] * (N + 1)
    # 클리어하지 못한 플레이어 수
    fail = [0] * (N + 1)
    
    # 각 스테이지 정보 카운트
    for i in stages:
        # 마지막 스테이지까지 클리어한 사용자
        if i == N + 1:
            for j in range(1, N + 1): arrival[j] += 1
            continue
        # 클리어 못한 플레이어 수
        fail[i] += 1
        # 각 스테이지 도달한 플레이어 수
        for j in range(1, i + 1):
            arrival[j] += 1
            
    # 실패율 계산
    for i in range(1, N + 1):
        # 스테이지에 도달한 사용자가 없으면 0
        if arrival[i] == 0: result = 0
        else : result = fail[i] / arrival[i]
        # 스테이지 정보와 같이 추가
        answer.append((i, result))
    
    # 실패율을 기준으로 정렬
    answer.sort(reverse=True, key=lambda x: x[1])
    
    return [i[0] for i in answer]