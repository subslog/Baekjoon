N = int(input())

num = list(map(int, input().split()))

prime_count = 0     # 소수 카운트

# 1이 있으면 제거
if 1 in num:
    num.remove(1)
# 입력된 값 소수 검사
for i in num:
    # 소수면 True 유지됨
    result = True
    # i의 제곱근 +1까지 반복
    for j in range(2, int(i ** (1/2)) + 1):
        # 약수가 있으면 소수가 아니다.
        if i % j == 0:
            result = False
    # 소수이면 +1
    if result:
        prime_count += 1

print(prime_count)