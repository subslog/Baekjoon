M, N = map(int, input().split())

# M이 1이면 1 더하기
if M == 1:
    M += 1

prime_check = [False] * (N + 1)  # 소수 체크(False면 소수)

# 2부터 N까지 소수 판단
for i in range(2, N + 1):
    if prime_check[i] == False:
        # 소수의 배수 True로 변경
        for j in range(i * 2, N + 1, i):
            prime_check[j] = True

# M부터 N까지 False인 요소가 소수
for i in range(M, N + 1):
    if prime_check[i] == False:
        print(i)