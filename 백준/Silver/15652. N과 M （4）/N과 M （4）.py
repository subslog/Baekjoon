def n_m(index, N, M):
    # M개 수열 뽑으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    # 이전 수열보다 작으면 수행 안한다.
    for i in range(1, N + 1):
        if i < a[index - 1]: continue
        a[index] = i
        n_m(index + 1, N, M)

N, M = map(int, input().split())
# M개 수열 뽑기 체크
a = [0] * 9
n_m(0, N, M)