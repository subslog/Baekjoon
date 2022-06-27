N = int(input())

P = [0] + list(map(int, input().split()))

d = [0] * (N + 1)
# 점화식 d[N] = max(d[N - i] + P[i])
for i in range(1, N + 1):
    for j in range(1, i + 1):
        d[i] = max(d[i], d[i - j] + P[j])
    
print(d[N])