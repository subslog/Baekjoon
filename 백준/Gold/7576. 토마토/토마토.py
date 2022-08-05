import sys
from collections import deque

M, N = map(int, input().split())

# 그래프 생성
a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 토마토 익는 날짜 계산 리스트
c = [[-1] * M for _ in range(N)]
# 익은 토마토를 큐에 넣는다.
q = deque()
for i in range(N):
    for j in range(M):
        if a[i][j] == 1:
            c[i][j] = 0         # 방문 체크
            q.append((i, j))    # 큐에 위치 삽입

# 인접 노드(상, 하, 좌, 우) 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    # 현재 노드
    x, y = q.popleft()
    # 인접 노드에서 방문 가능한 노드 방문
    for i in range(4):
        # 다음 방문 노드 좌표
        nx, ny = x + dx[i], y + dy[i]
        # 상자 크기를 벗어나지 않고, 덜 익었고, 방문하지 않았으면 큐에 삽입
        if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == 0 and c[nx][ny] == -1:
            # 현재 일수에서 다음날에 익으니까 +1
            c[nx][ny] = c[x][y] + 1
            q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if a[i][j] == 0 and c[i][j] == -1:
            print(-1)
            sys.exit()

print(max([max(i) for i in c]))