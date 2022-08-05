from collections import deque

S = int(input())

# 시간 가중치 계산
dist = [[-1] * (S + 1) for _ in range(S + 1)]

# 초기값
dist[1][0] = 0
q = deque()
q.append((1, 0))

# bfs 수행
while q:
    # 현재 화면, 클립보드에 이모티콘 수
    s, c = q.popleft()

    # 아직 방문 안했으면 복사
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    # 붙여넣은 수가 목표 이모티콘 이하고, 방문 안했으면 붙여넣기
    if s + c <= S and dist[s + c][c] == -1:
        dist[s + c][c] = dist[s][c] + 1
        q.append((s + c, c))
    # 이모티콘 1개 삭제
    if s - 1 >= 0 and dist[s - 1][c] == -1:
        dist[s - 1][c] = dist[s][c] + 1
        q.append((s - 1, c))

ans = -1
for i in range(S + 1):
    if dist[S][i] != -1 and ans == -1 or ans > dist[S][i]:
        ans = dist[S][i]

print(ans)