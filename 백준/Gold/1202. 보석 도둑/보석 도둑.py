import sys
import heapq

# 입력 초기값
N, K = map(int, input().split())
gems = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

# 무게 순으로 오름차순 정렬
gems.sort(key=lambda x: x[0])
bags.sort()

# 최대 보석 무게 계산
answer = 0
heap = []
i = 0
for b in bags:
    # 가방에 담을 수 있는 보석을 최대 힙으로 저장
    while i < N and gems[i][0] <= b:
        heapq.heappush(heap, -gems[i][1])
        i += 1
    # 가방에 담을 수 있는 보석 중 제일 비싼거를 담는다.
    if heap:
        answer += -heapq.heappop(heap)

print(answer)