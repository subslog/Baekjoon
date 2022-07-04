import sys

n = int(input())
grape = [0]

# 포도주의 양 저장
for _ in range(n):
    ml = int(sys.stdin.readline())
    grape.append(ml)

d = [[0, 0, 0] for _ in range(n + 1)]    # DP 결과 저장 리스트
# 초기값
d[1][1] = grape[1]

# 점화식 : D[N][i] = N번 째까지 마신 최대 포도주의 양
# D[N][0] = max(D[N-1][0], D[N-1][1], D[N-1][2]) -> 안마신다.
# D[N][1] = D[N][0] + grape[N] -> 첫번 째로 마신다.
# D[N][2] = D[N][1] + grape[N] -> 두번 째로 마신다.
for i in range(2, n + 1):
    d[i][0] = max(d[i - 1])
    d[i][1] = d[i - 1][0] + grape[i]
    d[i][2] = d[i - 1][1] + grape[i]

print(max(d[n]))