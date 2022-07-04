import sys

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())

    d = [[0, 0, 0] for i in range(n + 1)]    # DP 결과 저장 리스트
    sticker1 = [0] + list(map(int, sys.stdin.readline().split()))
    sticker2 = [0] + list(map(int, sys.stdin.readline().split()))

    # 점화식 : D[N][i] = 2*N번 째에서 뜯은 스티커의 최대값
    # D[N][0] = max(D[N-1][0], D[N-1][1], D[N-1][2]) -> 스티커를 뜯지 않음
    # D[N][1] = max(D[N-1][0], D[N-1][2]) -> 위쪽 스티커를 뜯는다.
    # D[N][2] = max(D[N-1][0], D[N-1][1]) -> 아래쪽 스티커를 뜯는다.
    for i in range(1, n + 1):
        d[i][0] = max(d[i - 1])
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + sticker1[i]
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + sticker2[i]

    print(max(d[n]))