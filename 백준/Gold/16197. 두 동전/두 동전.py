def game(cnt: int, p1: list, p2: list):
    """동전을 하나만 떨어뜨리기 위한 최소 횟수 구하는 함수"""
    global ans
    # 재귀 종료 조건 : 동전 겹칠 때, 버튼 11번 이상, 동전이 동시 추락
    if p1 == p2 or cnt > 10 or (board[p1[0]][p1[1]] == False and board[p2[0]][p2[1]] == False):
        return
    # 동전이 떨어지면 정답 갱신 후 재귀 종료
    if board[p1[0]][p1[1]] == False or board[p2[0]][p2[1]] == False:
        ans = min(ans, cnt)
        return

    # 1개 동전 인접 노드에 벽이 있거나 2개 동전 인접 노드에 벽이 없으면 재귀
    # 위로 이동
    if board[p1[0] - 1][p1[1]] == '#' and board[p2[0] - 1][p2[1]] != '#':
        game(cnt + 1, [p1[0], p1[1]], [p2[0] - 1, p2[1]])
    elif board[p1[0] - 1][p1[1]] != '#' and board[p2[0] - 1][p2[1]] == '#':
        game(cnt + 1, [p1[0] - 1, p1[1]], [p2[0], p2[1]])
    elif board[p1[0] - 1][p1[1]] != '#' and board[p2[0] - 1][p2[1]] != '#':
        game(cnt + 1, [p1[0] - 1, p1[1]], [p2[0] - 1, p2[1]])
    # 아래로 이동
    if board[p1[0] + 1][p1[1]] == '#' and board[p2[0] + 1][p2[1]] != '#':
        game(cnt + 1, [p1[0], p1[1]], [p2[0] + 1, p2[1]])
    elif board[p1[0] + 1][p1[1]] != '#' and board[p2[0] + 1][p2[1]] == '#':
        game(cnt + 1, [p1[0] + 1, p1[1]], [p2[0], p2[1]])
    elif board[p1[0] + 1][p1[1]] != '#' and board[p2[0] + 1][p2[1]] != '#':
        game(cnt + 1, [p1[0] + 1, p1[1]], [p2[0] + 1, p2[1]])
    # 오른쪽으로 이동
    if board[p1[0]][p1[1] + 1] == '#' and board[p2[0]][p2[1] + 1] != '#':
        game(cnt + 1, [p1[0], p1[1]], [p2[0], p2[1] + 1])
    elif board[p1[0]][p1[1] + 1] != '#' and board[p2[0]][p2[1] + 1] == '#':
        game(cnt + 1, [p1[0], p1[1] + 1], [p2[0], p2[1]])
    elif board[p1[0]][p1[1] + 1] != '#' and board[p2[0]][p2[1] + 1] != '#':
        game(cnt + 1, [p1[0], p1[1] + 1], [p2[0], p2[1] + 1])
    # 왼쪽으로 이동
    if board[p1[0]][p1[1] - 1] == '#' and board[p2[0]][p2[1] - 1] != '#':
        game(cnt + 1, [p1[0], p1[1]], [p2[0], p2[1] - 1])
    elif board[p1[0]][p1[1] - 1] != '#' and board[p2[0]][p2[1] - 1] == '#':
        game(cnt + 1, [p1[0], p1[1] - 1], [p2[0], p2[1]])
    elif board[p1[0]][p1[1] - 1] != '#' and board[p2[0]][p2[1] - 1] != '#':
        game(cnt + 1, [p1[0], p1[1] - 1], [p2[0], p2[1] - 1])

N, M = map(int, input().split())
# 보드 생성 및 동전의 위치 찾기
board = [[False] * (M + 2)]
position = []
ans = 11
for i in range(1, N + 1):
    board.append([False] + list(input()) + [False])
    # 코인이 있으면 위치 추가
    coin_cnt = list(filter(lambda x: board[-1][x] == 'o', range(1, M + 1)))
    if coin_cnt:
        position += [[i, c] for c in coin_cnt]
board.append([False] * (M + 2))

game(0, position[0], position[1])

if ans == 11: print(-1)
else: print(ans)