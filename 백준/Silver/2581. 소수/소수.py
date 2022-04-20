M = int(input())
N = int(input())

if M == 1:
    M += 1

prime_list = list(range(M, N + 1))

# 시간 복잡도를 줄이기 위해 
# N이 M의 2배 이상일 때만 에라토스테네스의 체 진행
if M * 2 <= N:
    # M부터 N의 제곱근 +1까지 반복
    for i in range(M, int(N ** (1/2)) + 1):
        mul = 2

        # i의 배수가 N보다 커질 때까지 반복
        while i * mul <= N:
            # i의 배수가 리스트에 있으면 제거
            if i * mul in prime_list:
                prime_list.remove(i * mul)
            mul += 1    # 배수 증가
# 소수 제거
# 반복문 안에서 리스트의 요소가 변하므로 슬라이싱으로 반복문 사용
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