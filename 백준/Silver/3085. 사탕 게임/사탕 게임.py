import sys

def len_check(temp_board: list) -> int:
    """최대 길이 구하는 함수"""
    max_len = 1 # 최대 길이

    for i in range(N):
        cnt = 1     # 행 최대 길이 카운트

        # i행에서 최대 길이 구하기
        for j in range(N - 1):
            # 현재 색과 다음 색이 같으면 카운트
            if temp_board[i][j] == temp_board[i][j + 1]:
                cnt += 1
            # 다르면 cnt 초기화
            else:
                cnt = 1
            # 카운트가 최대 길이보다 크면 업데이트
            if cnt > max_len: max_len = cnt
        
        cnt = 1     # 열 최대 길이 카운트

        # i열에서 최대 길이 구하기
        for j in range(N - 1):
            # 현재 색과 다음 색이 같으면 카운트
            if temp_board[j][i] == temp_board[j + 1][i]:
                cnt += 1
            # 다르면 cnt 초기화
            else:
                cnt = 1
            # 카운트가 최대 길이보다 크면 업데이트
            if cnt > max_len: max_len = cnt
    
    return max_len

N = int(input())
board = []
answer = 1

for _ in range(N):
    candy = list(sys.stdin.readline().rstrip())
    board.append(candy)

# 모든 요소를 비교
for i in range(N):
    for j in range(N):
        # 현재 요소와 아래 요소의 색이 다르면
        if i < N - 1 and board[i][j] != board[i + 1][j]:
            # 현재 요소와 아래 요소 변경
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            # 변경 후 최대 길이 확인
            tmp = len_check(board)
            if answer < tmp: answer = tmp
            # 보드 원상 복구
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        # 현재 요소와 오른쪽 요소의 색이 다르면
        if j < N - 1 and board[i][j] != board[i][j + 1]:
            # 현재 요소와 오른쪽 요소 변경
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            # 변경 후 최대 길이 확인
            tmp = len_check(board)
            if answer < tmp: answer = tmp
            # 보드 원상 복구
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(answer)