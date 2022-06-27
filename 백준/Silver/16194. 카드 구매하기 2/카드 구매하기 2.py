N = int(input())

P = [0] + list(map(int, input().split()))

d = [0] * (N + 1)
# 점화식 d[N] = min(d[N - i] + P[i])
for i in range(1, N + 1):
    d[i] = P[i]
    for j in range(1, i):
        d[i] = min(d[i], d[i - j] + P[j])
    
print(d[N])