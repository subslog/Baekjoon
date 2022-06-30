N = int(input())

d = [[0] * 10 for _ in range(N + 1)]
d[1] = [1] * 10

# 점화식 : D[N][L] = 길기가 N이고 마지막 수가 L인 오르막의 개수
# D[N][L] = sum(D[N - 1][0 ~ L])
for i in range(2, N + 1):
    for j in range(0, 10):
        d[i][j] += sum(d[i - 1][:j + 1])
        d[i][j] % 10007

print(sum(d[N]) % 10007)
