M, N = map(int, input().split())

# M이 1이면 +1
if M == 1:
    M += 1

for i in range(M, N + 1):
    if all(i % j for j in range(2, int(i ** 0.5) + 1)):
        print(i)