from collections import deque

# 인접 노드 방문 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[[-1] * (K + 1) for _ in range(M)] for _ in range(N)]

# 시작 위치 처리
queue = deque([(0, 0, 0, 1)])
dist[0][0][0] = 1
# bfs
while queue:
    # 현재 위치
    x, y, z, t = queue.popleft()
    # 인접 위치 방문
    for k in range(4):
        # 다음 방문 노드
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어나지 않으면
        if 0 <= nx < N and 0 <= ny < M:
            # 벽을 부수지 않고 방문
            if arr[nx][ny] == 0 and dist[nx][ny][z] == -1:
                dist[nx][ny][z] = dist[x][y][z] + 1
                queue.append((nx, ny, z, t * -1))
            # 벽을 부수고 방문
            if z < K and arr[nx][ny] == 1 and dist[nx][ny][z + 1] == -1:
                # 밤이면 머무른다.
                if t == -1:
                    queue.append((x, y, z, t * -1))
                # 낮이면 부수고 이동한다.
                else:
                    dist[nx][ny][z + 1] = dist[x][y][z] + 1
                    queue.append((nx, ny, z + 1, t * -1))
    # 밤이면 방문 처리
    if t == -1 and (x < N - 1 or y < M - 1):
        dist[x][y][z] += 1

answer = list(filter(lambda x: x != -1, dist[N - 1][M - 1]))

if answer:
    print(min(answer))
else:
    print(-1)