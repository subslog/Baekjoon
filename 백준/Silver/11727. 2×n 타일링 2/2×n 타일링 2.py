n = int(input())

d = [0] * 1001

# 초기값 설정
d[0] = d[1] = 1
# n까지 반복
for i in range(2, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n] % 10007)