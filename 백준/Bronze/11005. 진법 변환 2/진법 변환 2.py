N, B = map(int, input().split())

answer = ""

while N > 0:
    remainder = N % B   # 나머지
    N = N // B          # 몫

    # 나머지가 10보다 크면 문자로 변환
    if remainder >= 10:
        answer += chr(55 + remainder)
    else:
        answer += str(remainder)

print(answer[::-1])