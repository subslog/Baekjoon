import sys

check = [True] * 1000001    # 소수 체크
prime_list = []             # 소수 리스트
# 소수의 배수는 소수에서 제외(에러토스테네스의 체)
for i in range(2, 1000001):
    if check[i]:
        prime_list.append(i)
        for j in range(i * 2, 1000001, i):
            check[j] = False

T = int(input())

for _ in range(T):

    N = int(sys.stdin.readline())
    cnt = 0             # 골드바흐 파티션 카운트

    for i in prime_list:
        # N = A + B -> N - A = B 요소가 True면 소수
        if N - i > 1 and i <= N - i:
            if check[N - i]:
                cnt += 1
        else:
            break

    print(cnt)