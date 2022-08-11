from collections import deque
import sys

V = int(input())
graph = [[] for _ in range(V + 1)]  # 그래프 저장
# 그래프 생성
for i in range(1, V + 1):
    idx, *node = map(int, sys.stdin.readline().split())
    for j in range(0, len(node), 2):
        if node[j] != -1: graph[idx].append((node[j], node[j + 1]))

def bfs(a: list, x: int):
    """최대 길이를 구하는 bfs 함수"""
    dist = [0] * (V + 1)        # 거리 계산용
    check = [False] * (V + 1)   # 방문 체크용
    q = deque()                 # 방문 노드 저장 큐
    # 시작 노드
    check[x] = True
    dist[x] = 0
    q.append(x)         
    # bfs 수행
    while q:
        now = q.popleft()   # 현재 노드
        # 인접 노드 방문
        for i in graph[now]:
            # 방문 안했으면 방문 처리
            if check[i[0]] == False:
                check[i[0]] = True              # 방문 처리
                dist[i[0]] = dist[now] + i[1]   # 거리 계산
                q.append(i[0])                  # 큐에 삽입
    # 최대 길이 계산
    max = -1
    node = 1
    for i in range(1, V + 1):
        if max < dist[i]:
            max = dist[i]
            node = i
    
    return node, max

# 임의의 정점에서 가장 먼 노드 u를 구한다.
start, start_dist = bfs(graph, 1)
# u에서 가장 긴 먼 노드가 지름이다.
end, end_dist = bfs(graph, start)

print(end_dist)