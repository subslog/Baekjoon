N = int(input())

d = [0] * (N + 1) # DP 저장 리스트

# 점화식 : D[N] = min(D[N - i**2]) + 1
for i in range(1, N + 1):
    d[i] = i    # N의 제곱수 최대항은 N이다.
    # 루트 N까지 반복
    for j in range(1, int(i ** 0.5) + 1):
        # D[N - i**2] + 1 보다 크면 업데이트
        if d[i] > d[i - j*j] + 1: d[i] = d[i - j*j] + 1

print(d[N])