def next_permutation(arr: list, N: int):
    """다음 수열을 구하는 함수"""
    i = N - 1
    # A[i-1] < A[i]를 만족하는 가장 큰 i를 찾는다.
    while i > 0 and arr[i - 1] >= arr[i]: i -= 1
    # 내림차순 정렬된 수열로 False 반환
    if i <= 0: return False
    # i <= j 이면서 A[i - 1] < A[j]를 만족하는 가장큰 j 찾기
    last = i - 1
    for j in range(last + 1, N):
        if arr[last] < arr[j]:
            exchange = j
    # A[i-1]와 A[j]를 swap
    arr[last], arr[exchange] = arr[exchange], arr[last]
    # A[i]부터 순열을 뒤집는다.
    arr[last + 1:] = arr[-1:last:-1]

    return True

N = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0

# 다음 수열을 이용해 모든 경우의 수를 반복
while True:
    tmp = 0
    # |A[0] - A[1]| + ... + |A[N-2] + A[N-1]|
    for i in range(N - 1):
        tmp += abs(arr[i] - arr[i + 1])
    # 최대값 변경
    if tmp > answer:
        answer = tmp
    # 마지막 순열이면 종료
    if not next_permutation(arr, N):
        break

print(answer)