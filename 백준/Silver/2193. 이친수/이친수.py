N = int(input())

d = [[0] * 2 for i in range(N + 1)]

d[1][0], d[1][1] = 0, 1 # DP 초기값 설정

# 점화식 d[N][L] = N 자리 이친수의 개수, L은 마지막 수
# d[N][L] = d[N-1][1] + d[N-1][0] + d[N-1][1]
for i in range(2, N + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[N]))
