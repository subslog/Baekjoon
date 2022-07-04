N = int(input())

A = [0] + list(map(int, input().split()))

d = [0] * (N + 1) # DP 결과 저장 리스트

# 점화식 : D[N] = N번 째에서 끝나는 제일 큰 합
# D[N] = max(D[j]) + A[i]
for i in range(1, N + 1):
    d[i] = A[i]
    for j in range(i - 1, 0, -1):
        if A[j] < A[i] and d[j] > d[i] - A[i]:
            d[i] = d[j] + A[i]

print(max(d))