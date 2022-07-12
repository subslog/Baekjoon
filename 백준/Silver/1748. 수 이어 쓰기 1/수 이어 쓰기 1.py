N = input()

answer = 0      # 정답

# 1부터 10을 곱하며 N의 자리수까지 반복
for i in range(1, len(N) + 1):
    # 현재 자리수에서 최대값(9, 99, 999, ...)
    end = 10 ** i - 1
    # end가 N보다 크면 end를 N으로 변경
    if end > int(N): end = int(N)
    # (end - 이전 자리수 + 1) * 자리수 길이
    # 1~9 : (9 - 1 + 1) * 1
    # 10~99 : (99 - 10 + 1) * 2
    answer += (end - 10 ** (i - 1) + 1) * i

print(answer)