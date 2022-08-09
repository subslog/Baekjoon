from collections import deque

# 방문할 인접 노드 상대 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, +1]

N = int(input())
# 그래프 생성
a = [list(map(int, input().split())) for _ in range(N)]
# 방문 확인용
check = [[False] * N for _ in range(N)]
# 거리 계산용
dist = [[-1] * N for _ in range(N)]
# 섬 저장용 큐
dist_q = deque()

def distinction(x: int, y: int, cnt: int):
    """섬을 구분하는 함수"""
    # 시작 노드
    q = deque()
    q.append((x, y))
    check[x][y] = True
    a[x][y] = cnt
    dist[x][y] = 0
    dist_q.append((x, y))
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
                dist[nx][ny] = 0          # 자신의 섬은 거리가 0
                dist_q.append((nx, ny)) # 섬간의 거리 구할 때 사용
                q.append((nx, ny))

cnt = 0 # 섬 구분용
# 연결 링크 찾기
for i in range(N):
    for j in range(N):
        # 섬이고, 방문하지 않았으면 bfs 수행
        if a[i][j] and check[i][j] == False:
            cnt += 1
            distinction(i, j, cnt)
# 각 노드를 기준으로 거리 계산
while dist_q:
    x, y = dist_q.popleft() # 현재 노드
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않고, 바다면
        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1   # 현재 노드 가중치 +1
            a[nx][ny] = a[x][y]             # 바다를 섬으로 바꾼다.
            dist_q.append((nx, ny))

# 최소 거리 저장용
answer = 10000
# 인접한 노드를 비교
for i in range(N):
    for j in range(N):
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            # 범위를 넘지 않고, 섬이 다르면 거리 갱신
            if 0 <= x < N and 0 <= y < N and a[i][j] != a[x][y]:
                answer = min(answer, dist[i][j] + dist[x][y])

print(answer)