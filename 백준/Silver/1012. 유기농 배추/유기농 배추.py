from collections import deque
# 인접 노드 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def worm(x: int, y:int):
    """인접한 배추에 배추흰지렁이를 퍼뜨리는 함수"""
    # 시작 위치 큐에 삽입
    queue = deque([(x, y)])
    visited[x][y] = True
    # bfs 수행
    while queue:
        # 현재 노드
        x, y = queue.popleft()
        # 인접 노드 확인
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위를 벗어나지 않고, 배추가 있으면 지렁이를 퍼뜨린다.
            if 0 <= nx < M and 0 <= ny < N and ground[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 테스트 케이스 개수
T = int(input())
# 테스트 케이스 개수만큼 반복
for _ in range(T):
    # 배추밭의 크기와 배추의 개수
    M, N, K = map(int, input().split())
    # 방문 확인용
    visited = [[False] * N for _ in range(M)]
    # 배추밭 생성
    ground = [[0] * N for _ in range(M)]
    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        ground[x][y] = 1
    # 배추밭을 모두 확인
    answer = 0
    for i in range(M):
        for j in range(N):
            # 배추가 있고, 지렁이가 퍼지지 않았으면 지렁이를 두고, 카운트
            if ground[i][j] == 1 and visited[i][j] == False:
                worm(i, j)
                answer += 1
    # 필요한 배추흰지렁이 수
    print(answer)