def arr_num(x:int, y: int):
    """현재 노드가 존재하는 3*3 배열 위치 반환"""
    return (x // 3) * 3 + (y // 3)

def sudoku(cnt: int):
    # 정답 조건 : 마지막 숫자까지 확인 완료
    if cnt == 81:
        for row in board:
            print(*row)
        return True
    x = cnt // N    # x행
    y = cnt % N     # y열
    # 0이 아니면 다음 칸으로 이동
    if board[x][y] != 0:
        return sudoku(cnt + 1)
    else:
        # 0이면 1~9 까지 행, 열, 3*3 배열에 없는 숫자 삽입
        for i in range(1, 10):
            if c[x][i] == False and c2[y][i] == False and c3[arr_num(x, y)][i] == False:
                # 행, 열, 3*3 배열에 숫자 체크
                c[x][i] = c2[y][i] = c3[arr_num(x, y)][i] = True
                # 수도쿠에 번호 업데이트
                board[x][y] = i
                # 이 후의 수도쿠 규칙에도 만족하면 True 반환
                if sudoku(cnt + 1):
                    return True
                # 규칙에 어긋나면 다시 0 넣고 다음 숫자 진행
                board[x][y] = 0
                c[x][i] = c2[y][i] = c3[arr_num(x, y)][i] = False
    return False

N = 9
board = [list(map(int, input().split())) for _ in range(N)]
c = [[False] * 10 for _ in range(N)]    # 행에 숫자가 있는지 체크
c2 = [[False] * 10 for _ in range(N)]   # 열에 숫자가 있는지 체크
c3 = [[False] * 10 for _ in range(N)]   # 3*3 배열에 숫자가 있는지 체크

# 현재 있는 숫자 체크
for i in range(N):
    for j in range(N):
        # 0이 아니면 숫자 체크
        if board[i][j] != 0:
            c[i][board[i][j]] = True                # i 행에 숫자 체크
            c2[j][board[i][j]] = True               # j 열에 숫자 체크
            c3[arr_num(i, j)][board[i][j]] = True   # arr_num 번째 배열에 숫자 체크

sudoku(0)