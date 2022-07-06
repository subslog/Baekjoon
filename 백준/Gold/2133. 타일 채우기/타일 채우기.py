N = int(input())

d = [0] * 31

# 초기값
d[0], d[1], d[2], d[3] = 1, 0, 3, 0

# 점화식 : D[N] = 3 * D[N - 2] + 2 * D[N - 4] + 2 * D[N - 6] +  
for i in range(4, N + 1):
    d[i] = 3 * d[i - 2]
    for j in range(i - 4, -1, -2):
        d[i] += 2 * d[j]
    
print(d[N])