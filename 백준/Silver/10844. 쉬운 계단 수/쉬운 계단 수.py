N = int(input())

mod = 1000000000 # 나눌값
d = [[0] * 10 for _ in range(N + 1)]

# 초기값 설정(길이가 1인 계단 수)
for i in range(1, 10):
    d[1][i] = 1

# 점화식 d[N][L] = 길이가 N이고, 마지막 수가 L인 계단 수
# d[N][L] = d[N - 1][L - 1] + d[N - 1][L + 1] (L이 0, 9일 경우 예외 필요)
for i in range(2, N + 1):
    for j in range(0, 10):
        if j - 1 >= 0: d[i][j] += d[i - 1][j - 1]
        if j + 1 <= 9: d[i][j] += d[i - 1][j + 1]
        d[i][j] %= mod

print(sum(d[N]) % mod)