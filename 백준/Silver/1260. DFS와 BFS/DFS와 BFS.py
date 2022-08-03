import sys
from collections import deque

def dfs(visit: int):
    """dfs 함수"""
    # 방문 노드 체크 후 방문한 노드에 추가
    dfs_check[visit] = True
    dfs_ans.append(visit)
    # 인접 노드 재귀 호출
    for i in a[visit]:
        # 방문하지 않았으면 방문
        if dfs_check[i] == False:
            dfs_check[i] = True
            dfs(i)

def bfs(start: int):
    """bfs 함수"""
    # 방문 노드 저장용 큐
    q = deque()
    # 시작 노드
    bfs_check[start] = True
    q.append(start)
    # 큐가 없어질 때까지 반복
    while len(q) != 0:
        visit = q.popleft()     # 현재 노드
        bfs_ans.append(visit)   # 방문한 노드 저장
        # 인접 노드 큐에 추가
        for i in a[visit]:
            # 방문하지 않았으면 방문
            if bfs_check[i] == False:
                bfs_check[i] = True
                q.append(i)

N, M, V = map(int, input().split())

# dfs 체크 및 정답
dfs_check = [False] * (N + 1)
dfs_ans = []
# bfs 체크 및 정답
bfs_check = [False] * (N + 1)
bfs_ans = []
# 그래프 생성용 리스트
a = [[] for _ in range(N + 1)]

# 그래프 생성
for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    a[node1].append(node2)
    a[node2].append(node1)

# 연결 노드 오름차순 정렬
for i in range(N + 1): a[i].sort()

dfs(V)
print(*dfs_ans)
bfs(V)
print(*bfs_ans)