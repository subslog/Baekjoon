def n_m(index: list, N: int, M: int):
    # M개의 수열을 뽑았으면 출력 후 종료
    if index == M:
        print(*a[:index])
        return
    # 중복 있게 재귀
    for i in range(1, N + 1):
        a[index] = i
        n_m(index + 1, N, M)

N, M = map(int, input().split())

# M개 수열 뽑기 체크
a = [0] * 8
n_m(0, N, M)