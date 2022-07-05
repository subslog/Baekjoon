N = int(input())

A = [0] + list(map(int, input().split()))

d_l = [0] * (N + 1)   # DP 결과 저장 리스트(왼쪽)
d_r = [0] * (N + 1)   # DP 결과 저장 리스트(오른쪽)

# 점화식 : D_L[i] = max(A[j]) + 1 -> 왼쪽
for i in range(1, N + 1):
    d_l[i] = 1
    for j in range(i - 1, 0, -1):
        if A[j] < A[i] and d_l[j] >= d_l[i]:
            d_l[i] = d_l[j] + 1

# 점화식 : D_R[i] = max(A[j]) + 1 -> 오른쪽
for i in range(N, 0, -1):
    d_r[i] = 1
    for j in range(i + 1, N + 1):
        if A[j] < A[i] and d_r[j] >= d_r[i]:
            d_r[i] = d_r[j] + 1

print(sum(max(zip(d_l, d_r), key=lambda x:x[0]+x[1])) - 1)