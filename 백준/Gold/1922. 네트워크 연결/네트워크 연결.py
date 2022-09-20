import sys

def find_parent(parent: list, x: int):
    """x의 루트 노드를 찾는 함수"""
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent: list, a: int, b: int):
    """a와 b를 하나의 집합으로 합치는 함수"""
    # a와 b의 루트 노드를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 노드가 작은 것을 부모 노드로 설정
    parent[max(a, b)] = min(a, b)

# 초기값 입력
N = int(input())
M = int(input())
# 간선 입력 및 비용을 기준으로 오름차순 정렬
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
# 부모 노드를 자기 자신으로 초기화
parent = [i for i in range(N + 1)]

# 최소 신장 트리의 가중치를 구한다.
answer = 0
for edge in edges:
    a, b, cost = edge
    # 루트 노드가 같지 않으면 최소 신장 트리에 추가
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)