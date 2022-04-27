import sys

prime_list = [1] * 10001

# 에라토스테네스의 체를 통해 2 ~ 10000 사이의 소수 리스트 생성
for i in range(2, len(prime_list)):
    if prime_list[i]:
        prime_list[i * 2::i] = [0] * (10000 // i - 1)

# 테스트 케이스만큼 반복
for _ in range(int(input())):
    n = int(sys.stdin.readline())

    # 골드하브 파티션을 찾을 시작 수
    start = n // 2

    for i in range(start, 1, -1):
        # n - i가 소수이고, i도 소수이면 출력
        if prime_list[n - i] and prime_list[i]:
            print(i, n - i)
            break