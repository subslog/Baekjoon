T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    # 나머지 연산을 위해 -1
    x -= 1
    y -= 1

    for k in range(x, N * M, M):
        if k % N == y:
            print(k + 1)
            break
    else:
        print(-1)