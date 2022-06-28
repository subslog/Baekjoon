def go(num: int) -> int:
    """역추적 출력 함수"""

    if num == -1: return

    go(v[num])
    print(A[num], end=" ")

N = int(input())

A = list(map(int, input().split()))
d = [0] * N     # LIS 길이
v = [-1] * N    # 역추적 용도

for i in range(N):
    d[i] = 1    # 자기 자신 +1
    # 처음부터 i 요소까지 반복
    for j in range(i):
        # 현재 수열의 요소가 크고, LIS 길이도 길면
        if A[j] < A[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1 # LIS 업데이트
            v[i] = j        # 역추적을 위해 이전 인덱스 저장

answer = max(d)

print(answer)
go(d.index(answer))