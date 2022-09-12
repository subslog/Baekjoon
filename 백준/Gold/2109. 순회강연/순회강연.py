import heapq

# 초기 입력값
n = int(input())
day = 0
pays = []
for _ in range(n):
    pays.append(tuple(map(int, input().split())))
    day = max(day,  pays[-1][1])

# 일정 순으로 내림차순 정렬
pays.sort(key=lambda x: x[1], reverse=True)
# 최대 일정부터 1일까지 최대 강연료 선택
answer = 0
heap = []
idx = 0
# 최대 일정부터 1일까지 반복
for d in range(day, 0, -1):
    # d 일까지 처리해도되는 일정을 최대 힙에 넣는다.
    while idx < n and d <= pays[idx][1]:
        heapq.heappush(heap, -pays[idx][0])
        idx += 1
    # 가능한 일정 중에 최대 강연료를 추가
    if heap:
        answer += -heapq.heappop(heap)
    day -= 1

print(answer)