import sys
from collections import deque
INF = int(1e9)

# 초기값 입력
N, M, K, X = map(int, input().split())
# 각 도시 간 그래프 생성
road = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V = map(int, sys.stdin.readline().split())
    road[U].append(V)
# 도시 X에서 나머지 도시까지의 최단 거리 무한 처리
dist = [INF] * (N + 1)

# 출발 노드 처리
queue = deque([X])
dist[X] = 0
# bfs 수행
while queue:
    # 현재 노드
    now = queue.popleft()
    # 인접 노드 방문 처리
    for city in road[now]:
        # 방문하지 않았으면 방문
        if dist[city] == INF:
            dist[city] = dist[now] + 1
            queue.append(city)
# 최단 거리가 K이면 출력
check = True
for i in range(1, N + 1):
    if dist[i] == K:
        print(i)
        check = False
if check:
    print(-1)