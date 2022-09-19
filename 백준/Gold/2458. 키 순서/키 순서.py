import sys

# 초기값 입력
N, M = map(int, input().split())

# 노든 노드 False 초기화 및 자기 자신은 True 초기화
students = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            students[i][j] = True

# 간선 정보 입력 받기
for _ in range(M):
    # s -> e 학생은 키 비교 완료
    s, e = map(int, sys.stdin.readline().split())
    students[s][e] = True

# 자신 또는 k 번째 학생을 거쳐 비교가 가능한지 체크
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            students[i][j] = students[i][j] or (students[i][k] and students[k][j])

# 키 비교 가능한 학생 카운트
answer = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if students[i][j] or students[j][i]:
            cnt += 1
    if cnt == N:
        answer += 1

print(answer)