from collections import deque

# 이동 가능한 상대 좌표
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
# 초기 입력값
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
# 각 칸으로 이동하는 최소 이동 횟수
dist = [[-1] * N for _ in range(N)]

# 시작 노드
dist[r1][c1] = 0
queue = deque([(r1, c1)])
# bfs 수행
while queue:
    # 현재 노드
    x, y = queue.popleft()
    # 다음 이동할 칸
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        # 체스판을 벗어나지 않고, 방문하지 않았으면 방문
        if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(dist[r2][c2])