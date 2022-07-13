def n_m(index, N, M):
    """1~N까지 자연수 중에서 중복없이 M개 수열 고르기"""
    # M개가 되면 M개의 수열을 출력
    if index == M:
        print(*a[:index])
        return

    for i in range(1, N + 1):
        # 현재 사용 중인 수는 패스
        if c[i]: continue
        c[i] = True             # 사용하는 수로 체크
        a[index] = i            # 인덱스에 현재 수를 넣는다.
        n_m(index + 1, N, M)    # 다음 수열을 뽑는다.
        c[i] = False            # 사용 반납

N, M = map(int, input().split())

c = [False] * 10    # 사용하는 수 체크
a = [0] * 10        # M만큼 쌓을 인덱스

n_m(0, N, M)