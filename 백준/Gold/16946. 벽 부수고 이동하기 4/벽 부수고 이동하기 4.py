from collections import deque

def wall_move(x:int, y: int):
    """연결 그래프의 노드 수를 반환하는 함수"""
    grp = len(grp_cnt)  # 그룹 번호
    cnt = 1             # 그룹 노드 수

    # 시작 위치 처리
    queue = deque([(x, y)])
    check[x][y] = True
    grp_list[x][y] = grp
    # bfs 수행
    while queue:
        # 현재 좌표
        x, y = queue.popleft()
        # 상, 하, 좌, 우 방문
        for k in range(4):
            # 방문 좌표
            nx, ny = x + dx[k], y + dy[k]
            # 범위를 벗어나지 않고, 벽이 아니면서 방문하지 않았으면 방문
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and check[nx][ny] == False:
                cnt += 1
                check[nx][ny] = True
                grp_list[nx][ny] = grp
                queue.append((nx, ny))
    
    grp_cnt.append(cnt)

# 상, 하, 좌, 우 상대 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 입력값
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
grp_list = [[-1] * M for _ in range(N)]  # 연결 리스트 그룹 저장
grp_cnt = []                            # 연결 리스트 그룹 노드 수
check = [[False] * M for _ in range(N)] # 방문 처리용
# 연결 그래프를 구한다.
for i in range(N):
    for j in range(M):
        # 0이면 연결 그래프를 구하고, 노드 수를 반환한다.
        if arr[i][j] == 0 and check[i][j] == False:
            wall_move(i, j)

# 벽에서 이동 가능한 칸을 구한다.
for i in range(N):
    for j in range(M):
        # 0이면 0 출력
        if arr[i][j] == 0:
            print(0, end='')
        # 1이면 상, 하, 좌, 우를 확인해 연결 그래프 그룹의 노드 수를 출력
        if arr[i][j] == 1:
            grp_set = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                # 범위를 벗어나지 않고, 벽이 아니면 연결 리스트의 그룹을 추가한다.
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                    grp_set.add(grp_list[nx][ny])
            result = 1
            # 각 그룹의 노드 수를 더한다.
            for g in grp_set:
                result += grp_cnt[g]
            print(result % 10, end='')
    print()