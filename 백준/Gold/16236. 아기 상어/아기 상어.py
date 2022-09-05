from collections import deque

def fish_find(arr: list, x: int, y: int, size: int):
    """사냥할 물고기를 찾는 함수"""
    ans = []
    dist = [[-1] * N for _ in range(N)]
    # 시작 위치 처리
    queue = deque([(x, y)])
    dist[x][y] = 0

    while queue:
        # 현재 위치
        x, y = queue.popleft()
        # 방문 검사할 위치
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 공간을 벗어나지 않고, 방문하지 않았어야 한다.
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                # 빈 공간이거나 물고기와 상어의 크기가 같으면 이동만 한다.
                if arr[nx][ny] == 0 or arr[nx][ny] == size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                # 상어보다 작으면 먹을 수 있다.
                elif arr[nx][ny] < size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    ans.append((dist[nx][ny], nx, ny))
    # 먹을 수 있는 물고기가 없으면 None 반환
    if not ans:
        return None
    # 정렬 후 맨 앞에 있는 물고기가 제일 가까운 물고기
    ans.sort()
    return ans[0]

# 이동할 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

answer = 0  # 정답
size = 2    # 상어 크기
exp = 0     # 경험치
# 먹을 물고기가 없을 때까지 반복
while True:
    # 물고기 찾기
    fish = fish_find(space, x, y, size)
    # 물고기가 없으면 반복 종료
    if fish is None:
        break
    dist, nx, ny = fish
    space[nx][ny] = 0   # 물고기 먹기
    answer += dist      # 이동 시간
    exp += 1            # 경험치 증가
    # 레벨업
    if size == exp:
        size += 1
        exp = 0
    x, y = nx, ny   # 다음 출발 위치

print(answer)