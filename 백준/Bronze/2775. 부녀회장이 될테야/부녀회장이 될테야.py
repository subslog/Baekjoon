import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    floor = [list(range(1, n + 1))]     # 0층 1호~n호

    # (k-1)층 n호까지 생성
    for i in range(1, k):
        floor.append([None] * n)
        floor[i][0] = 1
        for j in range(1, n):
            floor[i][j] = floor[i - 1][j] + floor[i][j - 1]
    
    # k층 n호 = (k-1)층 1~n호 합 
    print(sum(floor[k - 1]))