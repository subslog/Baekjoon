from collections import deque

def area_check(arr: list, x: int, y: int, dist: list, d: int):
    """같은 구역을 구하는 함수"""
    # 시작 처리
    queue = deque([(x, y)])
    dist[x][y] = d
    # bfs
    while queue:
        # 현재 노드
        x, y = queue.popleft()
        # 상, 하, 좌, 우 노드 확인
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위를 벗어나지 않고, 같은 색이면서 방문하지 않았으면 방문
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] == arr[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]
                queue.append((nx, ny))

# 인접 노드 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
# 일반 사람이 보는 그리드
grid = [list(input()) for _ in range(N)]
dist = [[-1] * N for _ in range(N)]
# 적록색약이 보는 그리드
grid2 = [['G' if grid[i][j] == 'R' else grid[i][j] for j in range(N)] for i in range(N)]
dist2 = [[-1] * N for _ in range(N)]

# 구역 검사
cnt = cnt2 = 0
for i in range(N):
    for j in range(N):
        # 방문하지 않았으면 구역 찾기
        if dist[i][j] == -1:
            cnt += 1
            area_check(grid, i, j, dist, cnt)
        if dist2[i][j] == -1:
            cnt2 += 1
            area_check(grid2, i, j, dist2, cnt2)

print(cnt, cnt2)