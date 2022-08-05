from collections import deque

max = 200000            # 최대로 갈 수 있는 거리
c = [False] * (max + 1) # 방문 체크 리스트
dist = [-1] * (max + 1) # 가중치 저장 리스트

N, K = map(int, input().split())

# 시작 위치
c[N] = True
dist[N] = 0
q = deque()
q.append(N)

while q:
    now = q.popleft() # 현재 노드

    # -1칸, 1칸, *2칸 이동
    for next in [now - 1, now + 1, now * 2]:
        # 범위를 벗어나지 않고, 방문하지 않았으면 큐에 삽입
        if 0 <= next < max and c[next] == False:
            c[next] = True
            dist[next] = dist[now] + 1
            q.append(next)

print(dist[K])