def find_parent(parent: list, x: int):
    """루트 노드를 반환하는 함수"""
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent: list, a: int, b:int):
    """두 노드를 하나의 집합으로 합치는 함수"""
    # 두 노드의 루트 노드를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 노드를 루트 노드로 같는다.
    parent[max(a, b)] = min(a, b)

# 초기값 입력
N = int(input())
M = int(input())
# 부모 노드를 자기 자신으로 초기화
parent = [i for i in range(N + 1)]
# 간선 정보를 입력
edges = []
for i in range(N):
    edge = list(map(int, input().split()))
    # i 도시와 j 도시가 연결되어 있으면 그룹으로 묶는다.
    for j in range(N):
        if edge[j] == 1 and find_parent(parent, i + 1) != find_parent(parent, j + 1):
            union_parent(parent, i + 1, j + 1)

# 여행이 가능한지 확인
answer = 'YES'
travel = list(map(int, input().split()))
for i in range(1, M):
    if parent[travel[i - 1]] != parent[travel[i]]:
        answer = 'NO'
        break

print(answer)