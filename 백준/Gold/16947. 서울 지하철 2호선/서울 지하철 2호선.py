import sys
from collections import deque
sys.setrecursionlimit(10000)

N = int(input())

# 그래프 생성
a = [[] for _ in range(N)]
for _ in range(N):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)
# 방문 체크용
check = [0] * N

def dfs(x: int, p: int):
    """사이클을 찾는 함수"""
    # -2 : 싸이클 찾음(순환선에 속하지 않음)
    # -1 : 싸이클을 찾지 못함
    # 2 : 사이클 찾음(순환선에 속함)

    # 이미 방문했던 노드면 싸이클이다.
    # 싸이클의 시작 노드이므로 해당 노드 반환
    if check[x] == 1: return x

    check[x] = 1    # 방문 처리
    # dfs 수행
    for y in a[x]:
        # 이전 노드와 같으면 반복 건너뛰기
        if y == p: continue
        res = dfs(y, x)
        # 싸이클이지만, 순환 노드에 포함되지 않음
        if res == -2: return -2
        # 순환 노드에 포함됨
        if res >= 0:
            check[x] = 2
            # 사이클의 시작 노드로 돌아왔으면 -2 반환
            # 사이클 시작 전의 재귀는 순환선이 아니다.
            if x == res: return -2
            else: return res
    
    return -1
# 순환 노드 찾기
dfs(0, -1)

# 거리 계산용
dist = [0] * N
# 인접 노드 방문 큐
q = deque()

for i in range(N):
    # 순환선에 포함되었으면
    if check[i] == 2:
        dist[i] = 0 # 거리 0
        q.append(i) # 큐에 삽입
    # 순환선에 포함되지 않았으면 방문하지 않았다는 의미로 -1
    else:
        dist[i] = -1
# bfs 반복
while q:
    # 현재 노드
    now = q.popleft()
    # 방문하지 않은 노드 큐에 삽입
    for i in a[now]:
        if dist[i] == -1:
            dist[i] = dist[now] + 1 # 현재 노드 +
            q.append(i)             # 큐에 삽입

print(*dist)