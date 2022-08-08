import sys

# 방문할 인접 노드 상대 좌표(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

# 그래프 생성
a = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 방문 및 이동 횟수 확인용
dist = [[-1] * M for _ in range(N)]
def dfs(x: int, y: int, cnt: int):
    # 방문한 노드가 사이클을 이루면 True 반환되며 종료
    if dist[x][y] != -1: return cnt - dist[x][y] >= 4
    # 방문 노드 체크
    dist[x][y] = cnt


    # dfs 수행
    for i in range(4):
        # 다음 방문 노드
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않고, 현재와 다음 점이 같으면 다음 노드 방문
        if 0 <= nx < N and 0 <= ny < M and a[x][y] == a[nx][ny]:
            if dfs(nx, ny, cnt + 1): return True

    return False

for i in range(N):
    for j in range(M):
        if dist[i][j] == -1:
            if dfs(i, j, 0):
                print('Yes')
                sys.exit()

print('No')