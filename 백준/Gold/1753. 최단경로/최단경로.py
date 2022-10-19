import sys
import heapq
# 무한
INF = int(10e9)

def dijkstra(start: int, graph: list, dist: list):
    """시작 노드에서 모든 모드까지의 최단 거리를 구하는 함수"""
    # 최소 힙
    queue = []
    # 시작 노드 힙에 추가
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    # 큐가 빌 때까지 수행
    while queue:
        # 현재 최단 거리 노드
        d, now = heapq.heappop(queue)
        # 현재 노드가 처리된 적이 있으면 무시
        if dist[now] < d:
            continue
        # 현재 노드와 연결된 인접 노드 확인
        for g in graph[now]:
            # 현재 노드를 거쳐 가는 비용
            cost = d + g[1]
            # 현재 노드를 거져 가는게 더 짧으면 최소 힙에 삽입
            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heapq.heappush(queue, (cost, g[0]))

# 초기값 입력
V, E = map(int, input().split())
start_node = int(input())
# 그래프 생성
graph = [[] * (V + 1) for _ in range(V + 1)]
# 최단 거리 테이블(무한으로 초기화)
dist = [INF] * (V + 1)

# 간선 입력
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    # u -> v 작은 비용으로 추가
    graph[u].append((v, w))

# 최단 경로 계산
dijkstra(start_node, graph, dist)

for i in range(1, V + 1):
    if dist[i] != INF:
        print(dist[i])
    else:
        print('INF')