import sys

# 초기값 입력
R, C = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 최대 행복지수 경로 찾기
answer = ''
# 행이 홀수이면 오른쪽, 아래, 왼쪽, 아래, 오른쪽 방향으로 반복해 목적지에 도착 가능
if R % 2 == 1:
    for i in range(R):
        # 홀수 행이면 오른쪽으로 이동
        if i % 2 == 0:
            answer += 'R' * (C - 1)
            # 마지막 행이 아니면 아래쪽으로 이동
            if i != R - 1:
                answer += 'D'
        # 짝수 행이면 왼쪽으로 이동
        else:
            answer += 'L' * (C - 1)
            answer += 'D'
# 열이 짝수이면 아래, 오른쪽, 위, 오른쪽, 아래 방향으로 반복해 목적지에 도착 가능
elif C % 2 == 1:
    for i in range(C):
        # 홀수 열이면 아래로 이동
        if i % 2 == 0:
            answer += 'D' * (R - 1)
            # 마지막 열이 아니면 오른쪽으로 이동
            if i != C - 1:
                answer += 'R'
        # 짝수 열이면 위로 이동
        else:
            answer += 'U' * (R - 1)
            answer += 'R'
# 행과 열이 모두 짝수인 경우
# 행과 열이 모두 짝수이면 i + j가 홀수인 곳 중에서 최소값인 곳은 방문하지 않는다.
else:
    # 방문하지 않을 칸을 찾는다.
    x, y = 0, 1
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 == 1 and ground[i][j] < ground[x][y]:
                x, y = i, j
    # 방문할 수 없는 행 포함 2개 행이 남을 때까지 출발지와 목적지에서 2개 행씩 방문 처리 한다.
    x1, y1 = 0, 0           # 출발지 좌표
    x2, y2 = R - 1, C - 1   # 목적지 좌표
    path = ''               # 목적지에서 오는 경로
    # 2개 행이 남을 때까지 반복
    while x2 - x1 > 1:
        # 방문 처리할 행에 방문하지 않을 칸이 없는 행일 경우만 방문 처리
        # 출발지에서 2개 행 이동
        if x1 // 2 < x // 2:
            answer += 'R' * (C - 1)
            answer += 'D'
            answer += 'L' * (C - 1)
            answer += 'D'
            x1 += 2
        # 목적지에서 2개 행 이동
        if x // 2 < x2 // 2:
            path += 'R' * (C - 1)
            path += 'D'
            path += 'L' * (C - 1)
            path += 'D'
            x2 -= 2
    # 방문할 수 없는 열 포함 2개 열이 남을 때까지 출발지와 목적지에서 2개 열씩 방문 처리
    # 2개 열이 남을 때까지 반복
    while y2 - y1 > 1:
        # 방문 처리할 열에 방문하지 않을 칸이 없는 열일 경우만 방문 처리
        # 출발지에서 2개 열 이동
        if y1 // 2 < y // 2:
            answer += 'DRUR'
            y1 += 2
        # 목적지에서 2개 열 이동
        if y // 2 < y2 // 2:
            path += 'DRUR'
            y2 -= 2
    # 방문하지 않을 칸의 위치에 따라 마지막 방문 처리
    if y == y1:
        answer += 'RD'
    else:
        answer += 'DR'
    # 목적지에서 처리한 방문을 역순으로 더한다.
    answer += path[::-1]

print(answer)