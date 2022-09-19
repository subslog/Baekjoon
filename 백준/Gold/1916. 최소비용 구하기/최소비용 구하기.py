import sys
import heapq
INF = int(1e9)

def dijkstra(arr: list, start: int, dist: list):
    """start에서 모든 경로로 가는 최소 비용을 구하는 함수"""
    # 시작 노드 처리
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    # 최단 경로 계산
    while queue:
        # 현재 비용이 제일 작은 노드
        d, now = heapq.heappop(queue)
        # 이미 방문된 노드라면 건너뛴다.
        if dist[now] < d:
            continue
        # 현재 노드와 인접한 노드 확인
        for a in arr[now]:
            # 현재 노드를 거쳐 가는 비용이 작으면 업데이트
            cost = d + a[0]
            if cost < dist[a[1]]:
                dist[a[1]] = cost
                heapq.heappush(queue, (cost, a[1]))

# 초기값 입력 및 그래프 생성
N = int(input())
M = int(input())
citys = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    citys[s].append((d, e))
start, end = map(int, input().split())
# 모든 비용을 무한으로 설정
dist = [INF] * (N + 1)

# start -> end 최소 비용
dijkstra(citys, start, dist)
print(dist[end])