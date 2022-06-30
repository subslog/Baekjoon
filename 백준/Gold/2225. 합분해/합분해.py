N, K = map(int, input().split())

mod = 1000000000
d = [[0] * (N + 1) for _ in range(K + 1)]   # DP 저장 리스트
d[0][0] = 1                                 # 초기값

# 점화식 : D[K][N] = 정수 K개를 더해서 그 합이 N인 경우의 수
# D[K][N] = D[K-1][N-L] (L은 더한 수 중에 마지막 수)
for i in range(1, K + 1):
    for j in range(N + 1):
        for l in range(j + 1):
            d[i][j] += d[i - 1][j - l]
        d[i][j] %= mod

print(d[K][N])