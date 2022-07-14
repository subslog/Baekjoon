def next(arr: list, N: int):
    # A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다.
    i = N - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1

    # 내림차순으로 정렬되어 있으면 마지막 수열이다.
    if i == 0: return [-1]

    # i <= j이면서 A[i] < A[j]를 만족하는 가장 큰 j를 찾는다.
    last_idx = i - 1
    for j in range(last_idx + 1, N):
        if arr[last_idx] > arr[j]:
            exchange = j

    # A[i]와 A[j]를 swap
    arr[last_idx], arr[exchange] = arr[exchange], arr[last_idx]

    # A[i]부터 순열을 뒤집는다.
    arr[last_idx + 1:] = arr[-1:last_idx:-1]

    return arr

N = int(input())

seq = list(map(int, input().split()))
print(*next(seq, N))