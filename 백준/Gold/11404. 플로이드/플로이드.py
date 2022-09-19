import sys
INF = int(1e7) + 1

# 초기값 입력
N = int(input())
M = int(input())

# 모든 경로를 무한으로 초기화
citys = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신 -> 자기 자신 경로 0으로 설정
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            citys[i][j] = 0

# 간선 정보 입력(중복 경로가 존재하기 때문에 작은 값을 넣는다.)
for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    # 기존 비용와 현재 비용 중 작은 값으로 갱신
    citys[s][e] = min(citys[s][e], d)

# 플로이드 워셜 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # i -> j, i -> k -> j 비용 중 작은 비용으로 업데이트
            citys[i][j] = min(citys[i][j], citys[i][k] + citys[k][j])

# INF 비용을 0으로 변경
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if citys[i][j] == INF:
            citys[i][j] = 0

for row in range(1, N + 1):
    print(*citys[row][1:])