from collections import deque
import sys

N, M = map(int, input().split())

# 그래프 생성
a = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
# 노드 이동 카운트
c = [[0] * M for _ in range(N)]
# 다음 방문 노드 저장 큐
q = deque()

# 다음 방문하기 위한 상대 노드(위, 오, 아, 왼)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 처음 방문
c[0][0] = 1
q.append((0, 0))

while len(q) != 0:
    # 현재 노드
    x, y = q.popleft()
    # 인접 노드에서 방문 가능한 노드 큐에 삽입
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and a[nx][ny] and c[nx][ny] == 0:
            c[nx][ny] = c[x][y] + 1 # 비용을 계산하기 위해 현재 노드의 값에서 +1
            q.append((nx, ny))

print(c[N-1][M-1])