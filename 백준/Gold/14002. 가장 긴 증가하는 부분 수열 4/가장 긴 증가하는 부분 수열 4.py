N = int(input())

A = list(map(int, input().split()))
# dp 저장 변수([0]: 가장 긴 수열 길이 저장, [1]: 증가 수열 요소 저장)
d = [[0, []] for i in range(N)]

for i in range(N):
    d[i][0] = 1             # 자기 자신 +1
    d[i][1].append(A[i])    # 수열 요소 추가
    # 처음부터 i 요소까지 반복
    for j in range(i):
        # i 요소가 j 요소보다 크고, 현재 수열 길이보다 길면
        if A[j] < A[i] and d[i][0] < d[j][0] + 1:
            d[i][0] = d[j][0] + 1       # 수열 길이 업데이트
            d[i][1] = d[j][1] + [A[i]]  # 이전 증수 수열 + 현재 수열 요소

answer = max(d, key=lambda x:x[0])

print(answer[0])
print(*answer[1])