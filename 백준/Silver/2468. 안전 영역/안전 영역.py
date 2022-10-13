from collections import deque
# 인접 노드 상대 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x: int, y: int):
    """물에 잠기지 않은 안전한 영역 범위 조사"""
    # 시작 위치 큐에 삽입
    queue = deque([(x, y)])
    visited[x][y] = True
    # bfs 수행
    while queue:
        # 현재 노드
        x, y = queue.popleft()
        # 인접 노드 방문
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위를 벗어나지 않고, 물에 잠기지 않고, 방문하지 않았으면 방문
            if 0 <= nx < N and 0 <= ny < N and rain_area[nx][ny] > 0 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 초기값 입력
N = int(input())
# 지역 생성
area = [list(map(int, input().split())) for _ in range(N)]
# 지역의 최소, 최대 높이 찾기
min_height = 101
max_height = 0
for i in range(N):
    for j in range(N):
        min_height = min(min_height, area[i][j] - 1)
        max_height = max(max_height, area[i][j] + 1)

# 지역의 최소 높이부터 최대 높이까지 반복
answer = 0
for h in range(min_height, max_height):
    # 비가 내린 후 지역
    rain_area = [list(map(lambda x: x - h, a)) for a in area]
    # 방문 확인용
    visited = [[False] * N for _ in range(N)]
    # 안전 지역 카운트
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 안전 영역 범위 방문 처리
            if rain_area[i][j] > 0 and visited[i][j] == False:
                bfs(i, j)
                cnt += 1
    # 최대 안전 영역 수 갱신
    answer = max(answer, cnt)

print(answer)