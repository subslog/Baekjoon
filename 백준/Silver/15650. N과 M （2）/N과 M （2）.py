def n_m(index: list, N:int, M:int, start:int):
    """중복되지 않는 수열 출력 함수"""
    # M개 수열을 뽑으면 출력
    if index == M:
        print(*a[:index])
        return

    for i in range(start, N + 1):
        # 수열 뽑기
        a[index] = i
        # 다음 수열 뽑기
        # 중복 제거를 위해 다음 시작 숫자 +1
        n_m(index + 1, N, M, i + 1)

N, M = map(int, input().split())

a = [0] * 9     # M개 수열 뽑기용

n_m(0, N, M, 1)