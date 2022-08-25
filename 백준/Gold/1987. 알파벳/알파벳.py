def maximum_move(x: int, y: int, cnt: int):
    """말이 최대로 이동할 수 있는 거리 구하는 함수"""
    ans = cnt
    # 알파벳 인덱스로 변환 후 방문 처리
    check[ord(board[x][y]) - 65] = True
    # 상, 하, 좌, 우 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 보드 범위를 벗어나지 않으면
        if 0 <= nx < R and 0 <= ny < C:
            # 방문하지 않은 알파벳이면 방문
            if not check[ord(board[nx][ny]) - 65]:
                ans = max(ans, maximum_move(nx, ny, cnt + 1))
            
    # 방문 처리 회수
    check[ord(board[x][y]) - 65] = False

    return ans

# 초기 입력
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = [False] * 26    # 방문 알파벳 체크용

print(maximum_move(0, 0, 1))