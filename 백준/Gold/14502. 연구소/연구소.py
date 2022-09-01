from collections import deque
from itertools import combinations

def infection(x, y):
    """바이러스를 퍼뜨리는 함수"""

    # 시작 인덱스 방문 처리 및 큐 push
    queue = deque([(x, y)])
    check[x][y] = True
    # bfs
    while queue:
        # 현재 인덱스
        x, y = queue.popleft()
        # 바이러스 퍼지기
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위를 벗어나지 않고, 방문하지 않았는데 빈 칸이면 
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == False and laboratory[nx][ny] == 0:
                check[nx][ny] = True
                queue.append((nx, ny))

# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 입력값
N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]

# 0의 위치 확인
zero = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            zero.append((i, j))
# 3개의 벽을 세울 수 있는 조합
wall_combi = combinations(zero, 3)

answer = 0
for wall in wall_combi:
    # 방문 확인용
    check = [[False] * M for _ in range(N)]
    # 벽 세우기
    for w in wall:
        laboratory[w[0]][w[1]] = 1
    # 바이러스 퍼뜨리기
    for i in range(N):
        for j in range(M):
            # 바이러스면 bfs 수행
            if laboratory[i][j] == 2:
                infection(i, j)
            # 벽이면 방문 처리
            elif laboratory[i][j] == 1:
                check[i][j] = True
    # 안전 영역 수 카운트
    cnt = 0
    for c in check:
        cnt += c.count(False)
    answer = max(answer, cnt)
    # 벽 회수
    for w in wall:
        laboratory[w[0]][w[1]] = 0

print(answer)