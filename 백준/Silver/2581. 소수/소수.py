M = int(input())
N = int(input())

if M == 1:
    M += 1

prime_list = []

for i in range(M, N + 1):
    # 2부터 i의 제곱근 +1까지 반복
    # 약수가 없으면 소수 리스트에 추가
    if all(i % j for j in range(2, int(i ** (1/2)) + 1)):
        prime_list.append(i)

if len(prime_list):
    print(f'{sum(prime_list)}\n{min(prime_list)}')
else:
    print(-1)