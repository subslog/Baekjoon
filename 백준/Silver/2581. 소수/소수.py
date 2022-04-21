M = int(input())
N = int(input())

if M == 1:
    M += 1

prime_list = list(range(M, N + 1))

for i in prime_list[:]:
    # 2부터 i의 제곱근 +1까지 반복
    for j in range(2, int(i ** (1/2)) + 1):
        # 약수가 있으면 리스트에서 i를 제거하고 내부 for 문 종료
        if i % j == 0:
            prime_list.remove(i)
            break

if len(prime_list):
    print(f'{sum(prime_list)}\n{min(prime_list)}')
else:
    print(-1)