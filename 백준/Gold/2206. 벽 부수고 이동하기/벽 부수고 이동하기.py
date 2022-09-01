from collections import deque

# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 입력값
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 거리 계산용
# dist[x][y][0] : 벽 안부수고 이동한 거리
# dist[x][y][1] : 벽 부수고 이동한 거리
dist = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

# 시작 좌표 처리
queue = deque([(0, 0, 0)])
dist[0][0][0] = 1
# bfs 수행
while queue:
    # 현재 좌표
    x, y, z = queue.popleft()
    for k in range(4):
        # 이동할 좌표
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어나지 않고,
        if 0 <= nx < N and 0 <= ny < M:
            # 벽을 안부수고 이동
            if arr[nx][ny] == 0 and dist[nx][ny][z] == -1:
                dist[nx][ny][z] = dist[x][y][z] + 1
                queue.append((nx, ny, z))
            # 벽을 부수고 이동
            if z == 0 and arr[nx][ny] == 1 and dist[nx][ny][1] == -1:
                dist[nx][ny][1] = dist[x][y][0] + 1
                queue.append((nx, ny, 1))

if dist[N - 1][M - 1][0] != -1 and dist[N - 1][M - 1][1]  != -1:
    print(min(dist[N - 1][M - 1]))
elif dist[N - 1][M - 1][0] != -1:
    print(dist[N - 1][M - 1][0])
elif dist[N - 1][M - 1][1] != -1:
    print(dist[N - 1][M - 1][1])
else:
    print(-1)