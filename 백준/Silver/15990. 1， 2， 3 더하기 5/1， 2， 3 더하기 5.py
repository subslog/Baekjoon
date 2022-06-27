import sys

T = int(input())
mod = 1000000009

"""점화식 d[n][j] = n를 1, 2, 3의 합으로 나타내는 방법의수, 마지막에 사용한 수는 j
d[n][j] = d[n][1] + d[n][2] + d[n][3]
d[n][1] = d[n - 1][2] + d[n - 1][3]
d[n][2] = d[n - 2][1] + d[n - 2][3]
d[n][3] = d[n - 3][1] + d[n - 3][2]"""

d = [[0] * 4 for _ in range(1000001)]
d[1][1:4] = [1, 0, 0]
d[2][1:4] = [0, 1, 0]
d[3][1:4] = [1, 1, 1]

for i in range(4, 100001):
    d[i][1] = (d[i - 1][2] + d[i - 1][3]) % mod
    d[i][2] = (d[i - 2][1] + d[i - 2][3]) % mod
    d[i][3] = (d[i - 3][1] + d[i - 3][2]) % mod

for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(d[n]) % mod)