import sys
from collections import deque

# 다음 이동 가능한 상대 좌표
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

N = int(input())

for _ in range(N):
    I = int(input())

    now = tuple(map(int, sys.stdin.readline().split()))     # 현재 위치
    goal = tuple(map(int, sys.stdin.readline().split()))    # 목표 위치

    # 각 칸으로 가는데 걸리는 이동 횟수
    c = [[-1] * I for _ in range(I)]
    # 현재 위치 방문 체크
    c[now[0]][now[1]] = 0
    # 다음 방문 노드를 넣기 위한 큐
    q = deque()
    q.append(now)

    # bfs 수행
    while q:
        x, y = q.popleft()  # 현재 노드
        # 다음 방문 노드 큐에 삽입
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i] # 다음 방문 노드 좌표
            # 체스판을 벗어나지 안고, 방문하지 않았으면 큐에 삽입
            if 0 <= nx < I and 0 <= ny < I and c[nx][ny] == -1:
                # 현재 이동한 수 +1
                c[nx][ny] = c[x][y] + 1
                q.append((nx, ny))
                
    print(c[goal[0]][goal[1]])