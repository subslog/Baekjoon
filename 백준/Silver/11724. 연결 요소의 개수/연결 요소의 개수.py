import sys
sys.setrecursionlimit(1000000)

def dfs(visit: int):
    """dfs 함수"""
    # 방문 노드 체크
    check[visit] = True
    # 인접 노드 재귀 호출로 방문
    for i in a[visit]:
        # 방문하지 않은 노드라면 방문
        if check[i] == False:
            dfs(i)

N, M = map(int, input().split())

# 그래프 저장할 리스트
a = [[] for _ in range(N + 1)]
# 방문 노드 체크 리스트
check = [False] * (N + 1)
# 연결 요소 카운트
cnt = 0

# 그래프 생성
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    a[node1].append(node2)
    a[node2].append(node1)

# dfs 반복하여 연결 요소 찾기
for i in range(1, N + 1):
    # 방문하지 않은 노드면 dfs 수행 후 연결 요소 +1
    if check[i] == False:
        dfs(i)
        cnt += 1

print(cnt)