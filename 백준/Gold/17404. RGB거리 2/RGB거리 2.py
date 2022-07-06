import sys

N = int(input())

d_red = [[0, 0, 0] for _ in range(N + 1)]   # 빨강 시작
d_green = [[0, 0, 0] for _ in range(N + 1)] # 초록 시작
d_blue = [[0, 0, 0] for _ in range(N + 1)]  # 파랑 시작

A = list(map(int, sys.stdin.readline().split()))
# 초기값
d_red[1] = [A[0], 1001, 1001]
d_green[1] = [1001, A[1], 1001]
d_blue[1] = [1001, 1001, A[2]]

# 점화식 : D[N][L] = N개의 집을 칠하는 최소 비용, L은 마지막으로 칠한 색
# D[N][0] = D[N-1][1] + A[0]
# D[N][1] = D[N-1][0] + A[1]
for i in range(2, N + 1):
    A = list(map(int, sys.stdin.readline().split()))

    d_red[i][0] = min(d_red[i - 1][1], d_red[i - 1][2]) + A[0]
    d_red[i][1] = min(d_red[i - 1][0], d_red[i - 1][2]) + A[1]
    d_red[i][2] = min(d_red[i - 1][0], d_red[i - 1][1]) + A[2]

    d_green[i][0] = min(d_green[i - 1][1], d_green[i - 1][2]) + A[0]
    d_green[i][1] = min(d_green[i - 1][0], d_green[i - 1][2]) + A[1]
    d_green[i][2] = min(d_green[i - 1][0], d_green[i - 1][1]) + A[2]

    d_blue[i][0] = min(d_blue[i - 1][1], d_blue[i - 1][2]) + A[0]
    d_blue[i][1] = min(d_blue[i - 1][0], d_blue[i - 1][2]) + A[1]
    d_blue[i][2] = min(d_blue[i - 1][0], d_blue[i - 1][1]) + A[2]

print(min(d_red[N][1:3] + d_green[N][::2] + d_blue[N][:2]))