import sys
sys.setrecursionlimit(1000000)

def dfs(visit: int, c: int):
    """dfs 함수"""
    # 방문 및 그룹 저장
    group[visit] = c
    # 인접 노드 재귀 호출하여 방문
    for i in a[visit]:
        if group[i] == 0:
            dfs(i, 3 - c)

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    # 방문 노드 체크 및 그룹 저장 리스트
    group = [0] * (V + 1)
    # 그래프 저장 리스트
    a = [[] for _ in range(V + 1)]
    # 그래프 생성
    for i in range(E):
        node1, node2 = map(int, sys.stdin.readline().split())
        a[node1].append(node2)
        a[node2].append(node1)
    # dfs 수행
    for i in range(1, V + 1):
        if group[i] == 0:
            dfs(i, 1)
    # 이분 그래프인지 검사
    check = True
    for i in range(1, V + 1):
        for j in a[i]:
            # 현재 노드와 인접한 노드가 같은 그룹이면 이분 그래프가 아니다.
            if group[i] == group[j]:
                check = False

    if check: print("YES")
    else: print("NO")
