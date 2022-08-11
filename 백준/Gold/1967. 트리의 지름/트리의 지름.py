from collections import deque
import sys

n = int(input())
graph = [[] for i in range(n + 1)]  # 그래프 저장
# 그래프 생성
for i in range(n - 1):
    u, v, d = map(int, sys.stdin.readline().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

def bfs(x):
    """x 노드에서 가장 먼 노드와 길이를 반환하는 bfs 함수"""
    q = deque()                 # 방문 노드 큐
    check = [False] * (n + 1)   # 방문 체크용
    dist = [0] * (n + 1)        # 거리 저장용
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
                check[i[0]] = True              # 방문 체크
                dist[i[0]] = dist[now] + i[1]   # 거리 계산
                q.append(i[0])                  # 방문 노드 push
    # 최대값 계산
    max = -1
    node = 1
    for i in range(1, n + 1):
        if max < dist[i]:
            max = dist[i]
            node = i
    
    return node, max

# 임의의 노드에서 제일 먼 노드 u를 구한다.
start, start_dist = bfs(1)
# u 노드에서 제일 먼 노드의 길이가 지름이다.
end, end_dist = bfs(start)

print(end_dist)