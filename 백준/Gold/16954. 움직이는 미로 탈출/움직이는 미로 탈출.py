from collections import deque

# 이동 가능한 상대 위치(좌상, 상, 우상, 우, 우하, 하, 좌하, 좌, 유지)
dx = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
board = [list(input()) for _ in range(8)]                   # 체스판
check = [[[False] * 9 for _ in range(8)] for _ in range(8)]   # 방문 여부 체크
ans = 0

# 시작 위치 처리
queue = deque([(7, 0, 0)])
check[7][0][0] = True
# bfs
while queue:
    # 현재 위치
    x, y, t = queue.popleft()
    # 끝에 도달했으면 종료
    if x == 0 and y == 7:
        ans = 1
        break
    # 인접한 노드 방문
    for k in range(9):
        nx, ny = x + dx[k], y + dy[k]   # 다음 방문 노드
        nt = min(t + 1, 8)              # 8초가 지나면 모든 벽이 없어지니까 최대 8초 상태까지만 확인
        # 범위를 벗어나지 않으면 방문 검사
        if 0 <= nx < 8 and 0 <= ny < 8:
            # 다음 방문할 노드의 t, t-1 위 노드에 벽이 있으면 움직이지 못한다.
            if nx - t >= 0 and board[nx - t][ny] == '#': continue
            if nx - t - 1 >= 0 and board[nx - t - 1][ny] == '#': continue
            # 방문하지 않았으면 방문
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                queue.append((nx, ny, nt))

print(ans)