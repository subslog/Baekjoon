from collections import deque

# 방문할 인접 노드 상대 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, +1]

N = int(input())
# 그래프 생성
a = [list(map(int, input().split())) for _ in range(N)]
# 방문 확인용
check = [[False] * N for _ in range(N)]

def distinction(x: int, y: int, cnt: int):
    """섬을 구분하는 함수"""
    # 시작 노드
    q = deque()
    q.append((x, y))
    check[x][y] = True
    a[x][y] = cnt
    # bfs 수행
    while q:
        x, y = q.popleft()
        # 인접 노드 방문
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않고, 방문하지 않았으면
            if 0 <= nx < N and 0 <= ny < N and a[nx][ny] and check[nx][ny] == False:
                check[nx][ny] = True    # 방문 처리
                a[nx][ny] = cnt         # 섬 구분을 위해 값 변경
                q.append((nx, ny))

cnt = 0 # 섬 구분용
# 연결 링크 찾기
for i in range(N):
    for j in range(N):
        # 섬이고, 방문하지 않았으면 bfs 수행
        if a[i][j] and check[i][j] == False:
            cnt += 1
            distinction(i, j, cnt)

# 거리 계산용
dist = [[-1] * N for _ in range(N)]
# 최소 거리 저장용
answer = 10000
# 섬 간의 최소 거리 찾기
for l in range(1, cnt + 1):
    dist_q = deque()
    for i in range(N):
        for j in range(N):
            dist[i][j] = -1
            # 같은 섬은 0으로 처리
            if a[i][j] == l:
                dist[i][j] = 0
                dist_q.append((i, j))
    # 현재 섬에서 나머지 섬까지 거리 확인
    while dist_q:
        # 현재 노드
        x, y = dist_q.popleft()
        # 인접 노드 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않으면
            if 0 <= nx < N and 0 <= ny < N:
                # 바다라면 현재 노드의 가중치에서 +1
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    dist_q.append((nx, ny))
    # 최소 거리 찾기
    for i in range(N):
        for j in range(N):
            # 현재 섬과 다르면 거리 갱신
            if a[i][j] > 0 and a[i][j] != l:
                answer = min(answer, dist[i][j] - 1)

print(answer)