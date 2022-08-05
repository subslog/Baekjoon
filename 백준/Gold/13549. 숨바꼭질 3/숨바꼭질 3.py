from collections import deque

N, K = map(int, input().split())

max = 200000
check = [False] * max # 방문 체크 리스트
dist = [-1] * max     # 가중치 저장 리스트

# 시작 노드
check[N] = True
dist[N] = 0
q = deque()
q.append(N)
next_q = deque()

# BFS 진행
while q:
    # 현재 노드
    now = q.popleft()

    # 범위를 벗어나지 않고, 방문하지 않았으면 *2
    if now * 2 < max and check[now * 2] == False:
        check[now * 2] = True       # 방문 체크
        q.append(now * 2)           # 현재 큐에 삽입
        dist[now * 2] = dist[now]   # 가중치 +0
    # 범위를 벗어나지 않고, 방문하지 않았으면 -1 이동
    if now - 1 >= 0 and check[now - 1] == False:
        check[now - 1] = True           # 방문 체크
        next_q.append(now - 1)          # 다음 큐에 삽입
        dist[now - 1] = dist[now] + 1   # 가중치 +1
    # 범위를 벗어나지 않고, 방문하지 않았으면 -1 이동
    if now + 1 < max and check[now + 1] == False:
        check[now + 1] = True           # 방문 체크
        next_q.append(now + 1)          # 다음 큐에 삽입
        dist[now + 1] = dist[now] + 1   # 가중치 +1
    # 현재 큐가 비었으면 다음 큐로 업데이트
    if not q:
        q = next_q
        next_q = deque()

print(dist[K])