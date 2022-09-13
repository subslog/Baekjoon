def hanoi(n: int, x: int, y: int):
    """1 ~ n의 원판을 x에서 y로 이동하는 함수"""
    if n == 0:
        return
    hanoi(n - 1, x, 6 - x - y)
    print(f'{x} {y}')
    hanoi(n - 1, 6 - x - y, y)

# 초기값 입력
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)