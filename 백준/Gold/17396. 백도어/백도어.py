import sys
import heapq
INF = int(1e10) + 1

def dijkstra(arr: list, dist: list, start: int):
    """0 번째에서 N-1 번째로 가는 최소 비용을 구하는 함수"""
    # 시작 노드 처리
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    # 최소 거리 계산
    while queue:
        # 현재 최소 비용의 노드
        d, now = heapq.heappop(queue)
        # 이미 방문한 노드이면 건너뛴다.
        if dist[now] < d:
            continue
        # 인접 노드 거리 확인
        for a in arr[now]:
            # 현재 노드를 거쳐 가는게 더 빠르면 업데이트
            cost = d + a[1]
            if cost < dist[a[0]]:
                dist[a[0]] = cost
                heapq.heappush(queue, (cost, a[0]))

# 초기값 입력 및 그래프 생성
N, M = map(int, input().split())
ward = list(map(int, input().split()))
# 마지막 위치는 방문 가능 처리
ward[N - 1] = 0
bifurcation = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, sys.stdin.readline().split())
    # 와드가 없는 곳만 경로를 추가한다.(s <-> e 로가는 비용 d)
    if ward[s] == 0 and ward[e] == 0:
        bifurcation[s].append((e, d))
        bifurcation[e].append((s, d))
# 모든 경로의 비용을 무한 처리
dist = [INF] * N

# 0 -> N-1 최소 경로 계산
dijkstra(bifurcation, dist, 0)
# 방문할 수 없으면 -1, 아니면 최소 거리 출력
if dist[N - 1] == INF:
    print(-1)
else:
    print(dist[N - 1])