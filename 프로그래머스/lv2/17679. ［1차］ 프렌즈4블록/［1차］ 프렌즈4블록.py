def block_check(n: int, m: int, board: list):
    """지워지는 블록을 지우는 함수"""
    # 검사할 상대 좌표
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    # 지워질 블록의 위치를 저장
    pop_block = set()
    # 처음 블록부터 검사
    for i in range(n - 1):
        for j in range(m - 1):
            pop_temp = {(i, j)}
            for k in range(3):
                # 확인할 블록
                nx, ny = i + dx[k], j + dy[k]
                # 블록이 있으면서 현재 블록과 같으면 집합에 추가하고, 아니면 검사 종료
                if board[nx][ny] != 0 and board[i][j] == board[nx][ny]:
                    pop_temp.add((nx, ny))
                else:
                    break
            # 2*2 블록이 pop되면 지워질 블록에 추가
            else:
                pop_block |= pop_temp
    # 위 블록부터 지워지기 위해 정렬
    pop_block = sorted(pop_block, key=lambda x: (x[0], -x[1]))
    # 지워질 블록이 있으면 지우고, 뒤에 0으로 채운다.
    for block in pop_block:
        x, y = block
        del board[x][y]
        board[x].append(0)
    # 지워진 수 반환
    return len(pop_block)

def solution(m, n, board):
    answer = 0
    # 보드를 오른쪽으로 90도 회전
    board_r = [[board[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
    # 지워질 블록이 없을 때까지 반복
    cnt = 1
    while cnt:
        # 지워질 블록 확인
        cnt = block_check(n, m, board_r)
        answer += cnt

    return answer