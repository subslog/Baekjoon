import sys

# 초기값 입력
N = int(input())
ropes = [int(sys.stdin.readline()) for _ in range(N)]
# 로프 오름차순 정렬
ropes.sort()
# 작은 로프부터 제외하면서 들어올릴 수 있는 최대 중량을 구한다.
answer = 0
for i in range(N):
    # N, N-1, N-2, ..., 1개 로프를 사용할 때 최대 중량
    answer = max(answer, ropes[i] * (N - i))

print(answer)