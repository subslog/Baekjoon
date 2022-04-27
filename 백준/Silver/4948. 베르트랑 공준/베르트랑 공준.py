import sys

while True:
    # n 입력
    n = int(sys.stdin.readline())
    # n이 0이면 종료
    if n == 0:
        break
    # 0 ~ 2n까지 리스트 생성
    decimal = list(range(2 * n + 1))
    # 소수의 수 카운터
    count = 0
    # 2 ~ 2n까지 에라토스테네스의 체 진행
    for i in decimal[2:]:
        # 요소의 값이 0이 아니면 진행
        if decimal[i]:
            # i의 배수를 0으로 변환
            # 2n을 i로 나눈 몫이 2n까지 i 배수의 개수다.
            # 리스트 시작이 i * 2 부터니까 -1 한다.
            decimal[2 * i::i] = [0] * ((2 * n) // i - 1)
            # i가 n보다 크면 카운터 증가
            if i > n:
                count += 1
    print(count)