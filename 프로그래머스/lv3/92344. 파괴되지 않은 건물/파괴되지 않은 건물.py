def solution(board, skill):
    answer = 0
    row_size = len(board)
    col_size = len(board[0])
    accumulate = [[0] * (col_size + 1) for _ in range(row_size + 1)]
    # 모든 스킬을 확인
    for k in skill:
        a_d, r1, c1, r2, c2, degree = k
        # 공격이면 음수로 바꾼다.
        if a_d == 1:
            degree *= -1
        accumulate[r1][c1] += degree
        accumulate[r1][c2 + 1] += -degree
        accumulate[r2 + 1][c1] += -degree
        accumulate[r2 + 1][c2 + 1] += degree
    # 행 구간합 수행
    for i in range(row_size):
        for j in range(col_size - 1):
            accumulate[i][j + 1] += accumulate[i][j]
    # 열 구간합 수행
    for j in range(col_size):
        for i in range(row_size - 1):
            accumulate[i + 1][j] += accumulate[i][j]
    # 보드에 반영
    for i in range(row_size):
        for j in range(col_size):
            board[i][j] += accumulate[i][j]
            # 건물이 부서지지 않았으면 카운트
            if board[i][j] > 0:
                answer += 1

    return answer