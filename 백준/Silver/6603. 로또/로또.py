def n_m(index: list, N:int, M:int, start:int):
    """중복되지 않는 수열 출력 함수"""
    # M개 수열을 뽑으면 출력
    if index == M:
        print(*a[:index])
        return

    for i in range(start, N):
        # 수열 뽑기
        a[index] = S[i]
        # 다음 수열 뽑기
        # 중복 제거를 위해 다음 시작 숫자 +1
        n_m(index + 1, N, M, i + 1)

while True:
    k, *S = map(int, input().split())
    if k == 0: break    # k가 0이면 종료
    a = [0] * 9         # M개 수열 뽑기용
    n_m(0, k, 6, 0)
    print()