import sys

decimal = list(range(123456 * 2 + 1))

# 123456 * 2까지 에라토스테네스의 체 진행
for i in decimal[2:]:
    # 요소의 값이 0이 아니면 진행
    if decimal[i]:
        # i의 배수를 0으로 변환
        # 123456 * 2를 i로 나눈 몫이 123456 * 2까지 i 배수의 개수다.
        # 리스트 시작이 i * 2 부터니까 -1 한다.
        decimal[2 * i::i] = [0] * ((123456 * 2) // i - 1)

while True:
    # n 입력
    n = int(sys.stdin.readline())
    # n이 0이면 종료
    if n == 0:
        break
    # 소수의 수 카운터
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if decimal[i]:
            count += 1
    print(count)