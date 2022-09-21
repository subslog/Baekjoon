INF = int(1e9)

def solution(n, s, a, b, fares):
    # 모든 경로를 무한으로 초기화
    point = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신 -> 자기 자신 경로 0으로 설정
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                point[i][j] = 0
    
    # 간선 정보 입력
    for fare in fares:
        c, d, f = fare
        point[c][d] = f
        point[d][c] = f

    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # i -> j, i -> k -> j 중에 작은 요금으로 업데이트
                point[i][j] = min(point[i][j], point[i][k] + point[k][j])
    
    # a와 b가 각자 택시타고 갈 경우 요금
    answer = point[s][a] + point[s][b]
    # 각 노드까지 합승 후에 각자 택시탈 경우 계산
    for i in range(1, n + 1):
        if i == s: continue
        shared = point[s][i]    # 합승 요금
        A = point[i][a]         # A 개인 요금
        B = point[i][b]         # B 개인 요금
        answer = min(answer, shared + A + B)

    return answer