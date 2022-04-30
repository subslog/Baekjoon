import sys

# 수정할 컬러를 반환하는 함수
def coloring(line, start):
    count = 0

    for idx, color in enumerate(line):
        if idx % 2 == 0 and color != start:
            count += 1
        elif idx % 2 == 1 and color == start:
            count += 1
    
    return count

N, M = map(int, input().split())
# 보드를 저장할 리스트
chess_board = []
# 최소 컬러 변수
min_color = N * M

# 보드 입력
for i in range(N):
    chess_board += [sys.stdin.readline().strip()]

# 가로로 진행
for i in range(M - 7):
    # 세로로 진행
    for j in range(N - 7):
        # 수정할 컬러 카운트
        W_count = 0
        B_count = 0
        for repeat in range(j, j + 8):
            if repeat % 2 == 0:
                W_count += coloring(chess_board[repeat][i:i + 8], 'W')
                B_count += coloring(chess_board[repeat][i:i + 8], 'B')
            else:
                W_count += coloring(chess_board[repeat][i:i + 8], 'B')
                B_count += coloring(chess_board[repeat][i:i + 8], 'W')

        min_color = min(min_color, W_count, B_count)

print(min_color)