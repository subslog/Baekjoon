def game(cnt: int, x1: int, y1: int, x2: int, y2: int):
    """동전을 하나만 떨어뜨리기 위한 최소 횟수 구하는 함수"""
    global ans
    # 동전 추락 확인
    fall1 , fall2 = False, False
    if x1 < 0 or x1 >= N or y1 < 0 or y1 >= M:
        fall1 = True
    if x2 < 0 or x2 >= N or y2 < 0 or y2 >= M:
        fall2 = True
    # 재귀 종료 조건 : 동전 겹칠 때, 버튼 11번, 동전이 동시 추락
    if [x1, y1] == [x2, y2] or cnt == 11 or (fall1 and fall2):
        return
    # 동전이 1개만 떨어지면 정답 갱신 후 재귀 종료
    if fall1 or fall2:
        ans = min(ans, cnt)
        return
    # 동전 상, 하, 좌, 우 이동
    for k in range(4):
        nx1, ny1 = x1 + dx[k], y1 + dy[k]
        nx2, ny2 = x2 + dx[k], y2 + dy[k]
        # 이동하는 위치에 벽이 있으면 위치 초기화
        if 0 <= nx1 < N and 0 <= ny1 < M and board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < N and 0 <= ny2 < M and board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        # 재귀 호출
        game(cnt + 1, nx1, ny1, nx2, ny2)

# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
# 보드 생성 및 동전의 위치 찾기
board = []
position = []
ans = 11
for i in range(N):
    board.append(list(input()))
    # 코인이 있으면 위치 추가
    coin_cnt = list(filter(lambda x: board[-1][x] == 'o', range(M)))
    if coin_cnt:
        position += [[i, c] for c in coin_cnt]

game(0, position[0][0], position[0][1], position[1][0], position[1][1])

if ans == 11: print(-1)
else: print(ans)