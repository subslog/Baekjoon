def next_permutation(arr: list) -> bool:
    """다음 순열을 반환하는 함수"""
    i = len(arr) - 1
    # A[i-1] < A[i] 찾기
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    # 내림차순 정렬된 수열로 다음 순열이 없다.
    if i <= 0: return False

    # i <= j이면서 A[i-1] < A[j]를 만족하는 가장 큰 j 찾기
    last = i - 1
    for j in range(last + 1, len(arr)):
        if arr[last] < arr[j]:
            max_j = j
    
    # A[i-1]과 A[j]를 swap
    arr[last], arr[max_j] = arr[max_j], arr[last]

    # A[i]부터 순열 뒤집기
    arr[last + 1:] = arr[-1:last:-1]

    return True

N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]
d = list(range(N))  # 방문 순서
answer = 9000000

while True:
    path_check = True   # 방문 가능한 경로인지 확인
    sum = 0             # 방문 경로의 비용
    # N 번째까지 방문
    for i in range(N - 1):
        # w[i][j]가 0이면 방문 가능한 경로가 아니다.
        if w[d[i]][d[i + 1]] == 0:
            path_check = False
            break
        else:
            # 방문 경로 비용 더하기
            sum += w[d[i]][d[i + 1]]
    # N 번째까지 방문이 가능하고 출발지로 돌아갈 수 있으면 비용을 더하고, 최소 비용을 구한다.
    if path_check and w[d[-1]][d[0]] != 0:
        sum += w[d[-1]][d[0]]
        answer = min(answer, sum)
    # 다음 순열이 없으면 반복 종료
    if not next_permutation(d):
        break

print(answer)