import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]  # 그래프
parent = [0] * (N + 1)              # 부모 저장
# 그래프 생성
for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 시작 노드
q = deque()
q.append(1)
parent[1] = 1
# bfs 수행
while q:
    # 현재 노드
    now = q.popleft()
    # 인접 노드 방문
    for i in graph[now]:
        # 부모가 0이면 방문 안한 노드이므로 큐에 삽입
        if parent[i] == 0:
            q.append(i)     # 큐 삽입
            parent[i] = now # 부모 삽입

print('\n'.join(map(str, parent[2:])))