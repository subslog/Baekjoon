import sys
sys.setrecursionlimit(1000001)

def find_parent(parent: list, x: int):
    """x의 루트 노드를 반환하는 함수"""
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent: list, a: int, b: int):
    """a와 b를 하나의 집합으로 합치는 함수"""
    # a와 b의 루트 노드를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 작은 노드를 루트로 설정
    parent[max(a, b)] = min(a, b)

# 초기값 입력
n, m = map(int, input().split())
# 부모 노드를 자기 자신으로 초기화
parent = [i for i in range(n + 1)]
# 간선 정보를 입력
for _ in range(m):
    u_f, a, b = map(int, sys.stdin.readline().split())
    # 0이면 union, 1이면 find
    if u_f == 0:
        union_parent(parent, a, b)
    # 같은 집합이면 YES 출력
    elif find_parent(parent, a) == find_parent(parent, b):
        print('YES')
    # 아니면 NO 출력
    else:
        print('NO')