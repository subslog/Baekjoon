import sys
sys.setrecursionlimit(10000)

def land_check(x: int, y: int):
    """모든 방향을 확인해 섬을 구하기 위한 함수"""
    # 현재 노드 방문 체크
    c[x][y] = 1
    for i in range(8):
        # 다음 방문 확인 좌표
        next_x, next_y = x + dx[i], y + dy[i]
        # 방문하지 않고, 섬 크기의 범위를 벗어나지 않으면서 땅인 경우
        if 0 <= next_x < h and 0 <= next_y < w and a[next_x][next_y] and c[next_x][next_y] == 0:
            land_check(next_x, next_y)



# 왼위, 위, 오위, 오, 오아, 아, 왼아, 왼 상대 좌표
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

while True:
    w, h = map(int, sys.stdin.readline().split())
    # 입력이 0 0 이면 종료
    if w == h == 0: break
    
    # 방문 확인용 리스트
    c = [[0] * w for _ in range(h)]
    # 지도 생성
    a = []
    for _ in range(h):
        a.append(list(map(int, sys.stdin.readline().split())))
    # 섬 카운트
    cnt = 0
    for i in range(h):
        for j in range(w):
            # 현대 노드가 땅이고, 방문하지 않았으면 방문
            if a[i][j] and c[i][j] == 0:
                cnt += 1
                land_check(i, j)
    
    print(cnt)