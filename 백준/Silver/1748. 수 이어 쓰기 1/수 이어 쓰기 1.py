N = int(input())

answer = 0      # 정답
mod = 100000000 # 자리수 찾기용

# mod // 10 반복하며 0이되면 종료
while mod != 0:
    # N을 mod로 나눈 나머지값이 N보다 작으면 자리수 찾은거다.
    if N % mod < N:
        # 맨 왼쪽 수 (2345일 경우 2)
        first = int(str(N)[0]) - 1
        # 최상위 자리수만큼 곱하여 개수 플러스 (2345일 경우 1000 * 4 = 4000개)
        answer += first * mod * len(str(mod))
        # 나머지 자리수만큼 곱하여 개수를 더한다. (2345일 경우 345 * 4 = 1380개)
        answer += (N % mod + 1) * len(str(mod))
        # 두 번째 자리수의 최대값 (2345일 경우 1000 - 1 = 999)
        N = mod - 1
    mod //= 10

print(answer)