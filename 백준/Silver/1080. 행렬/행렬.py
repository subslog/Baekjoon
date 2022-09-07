N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        # 다르면 같아지기 위해 3*3 변환한다.
        if A[i][j] != B[i][j]:
            cnt += 1
            for i3 in range(i, i + 3):
                for j3 in range(j, j + 3):
                    A[i3][j3] ^= 1

if A == B:
    print(cnt)
else:
    print(-1)