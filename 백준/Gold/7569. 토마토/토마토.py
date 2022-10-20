from collections import deque
import sys
# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기값 입력
M, N, H = map(int, input().split())
# 익은 토마토를 저장할 큐
queue = deque()
# 각 토마토가 익는데 걸리는 날짜
day = [[[-1] * M for _ in range(N)]for _ in range(H)]
# 토마토 상자 생성
boxs = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
# 익은 토마토를 큐에 담는다.
for h in range(H):
    for i in range(N):
        for j in range(M):
            # 익은 토마토를 담는다.
            if boxs[h][i][j] == 1:
                queue.append((h, i, j))
                day[h][i][j] = 0
            # 토마토가 없으면 체크
            elif boxs[h][i][j] == -1:
                day[h][i][j] = -2

# bfs 수행
while queue:
    # 현재 위치
    h, x, y = queue.popleft()
    # 인접한 토마토를 익힌다.
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        # 박스를 벗어나지 않고, 익지 않은 토마토면 익힌다.
        if 0 <= nx < N and 0 <= ny < M and boxs[h][nx][ny] == 0 and day[h][nx][ny] == -1:
            queue.append((h, nx, ny))
            day[h][nx][ny] = day[h][x][y] + 1
    # 아래, 위 박스의 토마토를 익힌다.
    for k in range(-1, 2, 2):
        nh = h + k
        # 아래, 위 박스가 있고, 익지 않은 토마토면 익힌다.
        if 0 <= nh < H and boxs[nh][x][y] == 0 and day[nh][x][y] == -1:
            queue.append((nh, x, y))
            day[nh][x][y] = day[h][x][y] + 1

# 익는데 제일 오래 걸린 토마토를 찾는다.
answer = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            # 안익은 토마토가 있으면 -1 출력 후 종료
            if day[h][i][j] == -1:
                print(-1)
                exit()
            answer = max(answer, day[h][i][j])

print(answer)