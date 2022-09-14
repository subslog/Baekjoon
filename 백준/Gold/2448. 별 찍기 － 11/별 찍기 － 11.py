def star_remove(arr: list, N: int, x: int, y: int):
    """별을 제거하는 함수"""
    # 3 * 3 별 제거
    if N == 3:
        arr[x + 1][y + 2] = ' '
        return
    # 현재 크기에서 별 제거
    next_N = N // 2
    start = end = y + next_N
    for i in range(x + next_N, x + 2 * next_N):
        for j in range(start, end + N - 1):
            arr[i][j] = ' '
        start += 1
        end -= 1
    # 3개 별로 분할
    star_remove(arr, next_N, x, y + next_N)
    star_remove(arr, next_N, x + next_N, y)
    star_remove(arr, next_N, x + next_N, y + N)

# 초기값 입력
N = int(input())
arr = [['*'] * (N * 2) for _ in range(N)]

# 삼각형 별모양 만들기
for i in range(N):
    for j in range(N - i - 1):
        arr[i][j] = ' '
        arr[i][2 * N - j - 2] = ' '
    arr[i][2 * N - 1] = ' '

star_remove(arr, N, 0, 0)
for a in arr:
    print(''.join(a))