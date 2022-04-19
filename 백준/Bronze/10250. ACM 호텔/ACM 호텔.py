import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    ho = math.ceil(N / H)   # 호수 계산

    # 호수 문자열 변환
    if ho < 10:
        ho = '0' + str(ho)
    else:
        ho = str(ho)

    floor = N % H           # 층수 계산

    # 층수 문자열 변환
    if floor == 0:
        # 나머지 값이 0이면 최상위 층
        floor = str(H)
    else:
        floor = str(floor)

    print(floor + ho)