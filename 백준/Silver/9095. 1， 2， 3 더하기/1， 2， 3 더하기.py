import sys

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())

    d = [0] * 11                # 작은 문제 저장 리스트
    d[1], d[2], d[3] = 1, 2, 4  # 초기값 설정

    # n까지 점화식 반복
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    
    print(d[n])