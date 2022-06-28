A = int(input())

Ai = list(map(int, input().split()))
d = [0] * A

for i in range(A):
    d[i] = 1    # 자기 자신 +1
    # 처음부터 i 요소까지 반복
    for j in range(i):
        # i 요소가 j 요소보다 크고, 현재 수열 길이보다 길면 길이 업데이트
        if Ai[j] < Ai[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))