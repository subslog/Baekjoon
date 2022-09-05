from collections import deque

# 인접 노드 상대 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 방향 표시(상, 하, 좌, 우)
direction = [-1, -1, 1, 1]

W, H = map(int, input().split())
arr = [input() for _ in range(H)]
# 레이저 위치 파악
start, end = [(i, j) for i in range(H) for j in range(W) if arr[i][j] == 'C']
# 레이저 발사 횟수
dist = [[-1] * W for _ in range(H)]

# 시작 처리
queue = deque([(start[0], start[1])])
dist[start[0]][start[1]] = 0
# bfs 수행
while queue:
    # 현재 위치 및 방향
    x, y = queue.popleft()
    # 인접 노드 방문 확인
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어나거나 벽을 만날 때까지 끝까지 방문한다.
        while 0 <= nx < H and 0 <= ny < W:
            # 벽 만나면 종료
            if arr[nx][ny] == '*': break
            # 방문하지 않았으면 방문
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
            # 다음 인덱스
            nx += dx[k]
            ny += dy[k]

print(dist[end[0]][end[1]] - 1)