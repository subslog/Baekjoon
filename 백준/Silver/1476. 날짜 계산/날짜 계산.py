E, S, M = map(int, input().split())

E_cnt, S_cnt, M_cnt = 1, 1, 1   # 준규 나라 연도
year = 1                        # 지구 연도

while True:
    # 준규 나라 연도이면 지구 연도 출력 후 종료
    if E_cnt == E and S_cnt == S and M_cnt == M:
        print(year)
        break
    
    # +1년
    E_cnt += 1
    S_cnt += 1
    M_cnt += 1
    year += 1

    # 연도 범위 초과 시 초기화
    if E_cnt >= 16:
        E_cnt = 1
    if S_cnt >= 29:
        S_cnt = 1
    if M_cnt >= 20:
        M_cnt = 1