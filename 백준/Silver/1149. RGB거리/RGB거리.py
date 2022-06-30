import sys

N = int(input())
color = [0]

for _ in range(N):
    color.append(list(map(int, sys.stdin.readline().split())))

d = [[0] * 3 for _ in range(N + 1)]     # DP 저장 리스트
d[1][0], d[1][1], d[1][2] = color[1]    # 초기값

# 점화식 : D[N][L] = N개의 집을 칠하는 최소 비용, L은 마지막으로 칠한 집
# D[N][빨] = min(D[N-1][초], D[N-1][파])
# D[N][초] = min(D[N-1][빨], D[N-1][파])
# D[N][파] = min(D[N-1][빨], D[N-1][초])
# D[N][L] = min()
for i in range(2, N + 1):
    # N번 집 칠하는 비용으로 변경
    d[i][0], d[i][1], d[i][2] = color[i]
    # D[N][L] 계산
    d[i][0] += min(d[i - 1][1], d[i - 1][2])
    d[i][1] += min(d[i - 1][0], d[i - 1][2])
    d[i][2] += min(d[i - 1][0], d[i - 1][1])

print(min(d[N]))