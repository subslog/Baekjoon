def prime_num(num: int) -> bool:
    """소수 판별 함수"""
    # 2보다 작으면 소수 아님
    if num < 2:
        return False
    # 루트 n까지 num으로 나누어 떨어지지 않으면 소수
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

answer = 0  # 소수 카운트

N = int(input())

num_list = list(map(int, input().split()))

for num in num_list:
    if prime_num(num):
        answer += 1

print(answer)