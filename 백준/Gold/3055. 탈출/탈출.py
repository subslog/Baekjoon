from collections import deque

# 이동할 상대 좌표(상, 하, 좌, 우, 유지)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
t_map = [input() for _ in range(R)]
# 비버 굴, 고슴도치, 물 위치 찾기
warter_queue = deque()
warter_time = [[-1] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if t_map[i][j] == 'D':
            house = (i, j)
        elif t_map[i][j] == 'S':
            hedgehog = (i, j)
        elif t_map[i][j] == '*':
            warter_queue.append((i, j))
            warter_time[i][j] = 0

# 물 차는 시간
while warter_queue:
    # 현재 노드
    x, y = warter_queue.popleft()
    # 인접 노드 확인
    for k in range(4):
        # 다음 방문 노드
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어나지 않고, 비버 굴과 돌이 아니면 물이 찬다.
        if 0 <= nx < R and 0 <= ny < C and not t_map[nx][ny] in ['X', 'D'] and warter_time[nx][ny] == -1:
            warter_time[nx][ny] = warter_time[x][y] + 1
            warter_queue.append((nx, ny))

# 고슴도치 출발
dist = [[-1] * C for _ in range(R)]
hedgehog_queue = deque([hedgehog])
dist[hedgehog[0]][hedgehog[1]] = 0
ans = 'KAKTUS'
# bfs
while hedgehog_queue:
    # 현재 노드
    x, y = hedgehog_queue.popleft()
    # 비버 굴에 도착하면 종료
    if x == house[0] and y == house[1]:
        ans = dist[house[0]][house[1]]
        break
    # 인접노드 확인
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어나지 않고, 돌이 아니면서 방문하지 않았으면
        if 0 <= nx < R and 0 <= ny < C and t_map[nx][ny] != 'X' and dist[nx][ny] == -1:
            # 이동 후에도 물에 잠기지 않으면 이동
            if dist[x][y] + 1 < warter_time[nx][ny] or warter_time[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                hedgehog_queue.append((nx, ny))

print(ans)