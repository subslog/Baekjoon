def coin_change(coin: str):
    if coin == 'H':
        return 'T'
    else:
        return 'H'
    
# 초기 입력값
N = int(input())
coin_board = [list(input()) for _ in range(N)]

ans = N * N
# 2 ** N 가지의 케이스(0 ~ N-1 행까지 뒤집기 여부)
for case in range(1 << N):
    # 한 가지 케이스에서 T의 수
    T_cnt = 0
    for j in range(N):
        # j 열에서 T의 수
        cnt = 0
        for i in range(N):
            coin = coin_board[i][j]
            # i 행을 뒤집는 케이스면 뒤집기
            if (case & (1 << i)) != 0:
                coin = coin_change(coin)
            # T 카운트
            if coin == 'T':
                cnt += 1
        # j 열에 T의 수가 적은 케이스를 고른다.(뒤집기 또는 안뒤집기)
        T_cnt += min(cnt, N - cnt)
    # 최소 T 개수 업데이트
    ans = min(ans, T_cnt)

print(ans)