import sys

prime_check = [True] * 1000001  # 소수 체크(True면 소수)
prime_list = []                 # 소수 리스트

# 1000001까지 소수 구하기
for i in range(2, 1000001):
    # True면 소수 리스트에 추가
    if prime_check[i]:
        prime_list.append(i)
        # 소수의 배수는 False로 변경
        for j in range(i * 2, 1000001, i):
            prime_check[j] = False

while True:
    n = int(sys.stdin.readline())    # 입력 정수

    if n == 0:
        break

    answer = []         # 정답 리스트

    # 2 ~ 1000001 사이의 소수로 더하기 반복
    for prime in prime_list:
        # n = a + b -> n - a = b -> b가 소수이면 정답
        if prime_check[n - prime]:
            print(f"{n} = {prime} + {n - prime}")
            break
    else:
        print("Goldbach's conjecture is wrong.")