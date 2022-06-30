import sys

N = 1000001
d = [0] * N
d[1], d[2], d[3] = 1, 2, 4

# 점화식 : D[N] = D[N-1] + D[N-2] + D[N-3]
for i in range(4, N):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())

    print(d[n])