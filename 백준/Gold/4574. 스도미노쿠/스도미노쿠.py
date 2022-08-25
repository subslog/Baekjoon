def square(x: int, y: int):
    """몇 번째 3*3 배열인지 반환하는 함수"""
    return (x // 3) * 3 + (y // 3)
def check_num(x: int, y: int, num: int, condition: bool):
    """행, 열, 3*3 배열에 숫자를 체크하는 함수"""
    c[x][num] = condition
    c1[y][num] = condition
    c2[square(x, y)][num] = condition
def convert(string: str):
    """LU, LV 좌표를 반환하는 함수"""
    return (ord(string[0]) - 65, ord(string[1]) - 49)
def domino_check(x, y, num):
    """행, 열, 3*3 배열에 num 존재 확인 함수"""
    return not c[x][num] and not c1[y][num] and not c2[square(x, y)][num]
def sudominoku(cnt: int):
    """수노미노쿠를 처리하는 함수"""
    # 정답 조건 : 81까지 카운트되면 모든 보드를 채운 것이다.
    if cnt == 81:
        for i in range(9):
            print(''.join(map(str, board[i])))
        return True
    # 현재 보드 위치
    x = cnt // 9
    y = cnt % 9
    # 보드에 숫자가 있으면 다음 칸 확인
    if board[x][y] != 0:
        return sudominoku(cnt + 1)
    else:
        for k in range(2):
            nx, ny = x + dx[k], y + dy[k]   # 도미노 두 번째 칸 위치
            # 스도쿠 범위를 벗어나면 놓지 못하는 방향이다.
            if not (0 <= nx < 9 and 0 <= ny < 9):
                continue
            # 도미노 놓을 칸에 숫자가 있으면 놓지 못하는 방향이다.
            if board[nx][ny] != 0:
                continue
            # 도미노 놓기
            for i in range(1, 10):
                for j in range(1, 10):
                    # 도미도의 숫자가 같을 수는 없다. 또한 이미 사용한 도미노면 건너뛴다.
                    if i == j or domino[i][j]:
                        continue
                    # 도미노를 놓을 행, 열, 3*3 배열에 i, j 모두 없으면 놓는다.
                    if domino_check(x, y, i) and domino_check(nx, ny, j):
                        # 행, 열, 3*3 배열에 숫자 체크 및 도미도 사용 체크
                        check_num(x, y, i, True)
                        check_num(nx, ny, j, True)
                        domino[i][j] = domino[j][i] = True
                        # 보드에 숫자 업데이트
                        board[x][y], board[nx][ny] = i, j
                        # 수도쿠 조건을 만족하지 않으면 해당 숫자는 놓을 수 없기에 다음 숫자 찾기
                        if sudominoku(cnt + 1):
                            return True
                        # 행, 열, 3*3 베열, 도미모 반환
                        check_num(x, y, i, False)
                        check_num(nx, ny, j, False)
                        domino[i][j] = domino[j][i] = False
                        board[x][y] = board[nx][ny] = 0
    # 스도쿠 진행이 불가능하면 False 반환
    return False
# 도미노 놓을 방향을 확인하기 위한 상대 좌표
dx = [1, 0]
dy = [0, 1]
p_num = 1
while True:
    N = int(input())
    if N == 0: break
    test = 0
    c = [[False] * 10 for _ in range(10)]       # 행 체크
    c1 = [[False] * 10 for _ in range(10)]      # 열 체크
    c2 = [[False] * 10 for _ in range(10)]      # 3*3 배열 체크
    domino = [[False] * 10 for _ in range(10)]  # 도미노 체크
    board = [[0] * 9 for _ in range(9)]         # 스도쿠 저장
    # 도미노 놓기
    for _ in range(N):
        U, LU, V, LV = input().split()
        U, V = int(U), int(V)
        Ux, Uy = convert(LU)
        Vx, Vy = convert(LV)
        board[Ux][Uy] = U
        board[Vx][Vy] = V
        domino[U][V] = domino[V][U] = True
        check_num(Ux, Uy, U, True)
        check_num(Vx, Vy, V, True)
    # 1~9 놓기
    num = input().split()
    for i in range(1, 10):
        x, y = convert(num[i - 1])
        board[x][y] = i
        check_num(x, y, i, True)

    print(f'Puzzle {p_num}')
    p_num += 1
    sudominoku(0)