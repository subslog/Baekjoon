N = int(input())

A = [0] + list(map(int, input().split()))

d = [0] * (N + 1)

for i in range(1, N + 1):
    d[i] = 1
    for j in range(i - 1, 0, -1):
        if A[j] > A[i] and d[j] >= d[i]:
            d[i] = d[j] + 1

print(max(d))