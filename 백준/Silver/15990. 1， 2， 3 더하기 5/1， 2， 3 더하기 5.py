import sys

T = int(input())
mod = 1000000009

"""점화식 d[n][j] = n를 1, 2, 3의 합으로 나타내는 방법의수, 마지막에 사용한 수는 j
d[n][j] = d[n][1] + d[n][2] + d[n][3]
d[n][1] = d[n - 1][2] + d[n - 1][3]
d[n][2] = d[n - 2][1] + d[n - 2][3]
d[n][3] = d[n - 3][1] + d[n - 3][2]"""

d = [[0] * 4 for _ in range(1000001)]

for i in range(1, 100001):
    if i - 1 >= 0:
        d[i][1] = (d[i - 1][2] + d[i - 1][3]) % mod
        if i == 1: d[i][1] = 1  # d[0][1] = d[0][2] + d[0][3] = 2 예외 처리
    if i - 2 >= 0:
        d[i][2] = (d[i - 2][1] + d[i - 2][3]) % mod
        if i == 2: d[i][2] = 1  # d[0][2] = d[0][1] + d[0][3] = 2 예외 처리
    if i - 3 >= 0:
        d[i][3] = (d[i - 3][1] + d[i - 3][2]) % mod
        if i == 3: d[i][3] = 1  # d[0][3] = d[0][1] + d[0][2] = 2 예외 처리

for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(d[n]) % mod)
