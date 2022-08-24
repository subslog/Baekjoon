def check(row: int, col: int):
    # 열에 퀸이 있으면 False
    if check_col[col]:
        return False
    # / 대각선에 퀸이 있으면 False
    if check_dig1[row + col]:
        return False
    # \ 대각선에 퀸이 있으면 False
    if check_dig2[row - col + N-1]:
        return False
    return True

def queen(row: int):
    """퀸을 N개 놓을 수 있는 경우의 수를 반환하는 함수"""
    # 정답 추가 조건 : 퀸이 N개 놓일 경우
    if row == N:
        global ans
        ans += 1
        return
    # 열 반복
    for col in range(N):
        # 열, 대각선 방향에 퀸이 없으면 놓기
        if check(row, col):
            check_col[col] = True               # col 열에 퀸 못놓게 체크
            check_dig1[row + col] = True        # / 방향에 퀸 못놓게 체크
            check_dig2[row - col + N-1] = True  # \ 방향에 퀸 못놓게 체크
            queen(row + 1)                      # 다음 행 퀸 확인
            check_col[col] = False              # col 열에 퀸 반납
            check_dig1[row + col] = False       # / 방향에 퀸 반납
            check_dig2[row - col + N-1] = False # \ 방향에 퀸 반납
        
N = int(input())

check_col = [False] * N             # 열 방향 확인용
check_dig1 = [False] * (2 * N - 1)  # / 대각선 방향 확인용
check_dig2 = [False] * (2 * N - 1)  # \ 대각선 방향 확인용
ans = 0

queen(0)

print(ans)