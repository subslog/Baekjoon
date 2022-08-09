import sys
from collections import deque

N = int(input())
# 그래프 생성
a = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

order = list(map(lambda x: int(x) - 1, input().split()))

check = [False] * N # 방문 확인용
parent = [-1] * N   # 부모 노드 확인용

# 시작 노드 큐에 삽입
q = deque()
q.append(0)
check[0] = True
# 검사를 시작할 인덱스
m = 1
# bfs 검사 시작
for i in range(N):
    # 반복이 종료되기 전에 큐가 비면 방문 순서가 잘못됐다.
    if not q:
        print(0)
        sys.exit(0)

    x = q.popleft() # 현재 노드
    # 현재 노드와 입력 받은 방문 순서의 노드가 다르면
    if x != order[i]:
        print(0)
        sys.exit(0)

    cnt = 0 # x 노드를 부모로 가지는 노드 카운트
    for y in a[x]:
        # 방문하지 않은 노드면 부모 노드 추가 및 카운트
        if check[y] == False:
            parent[y] = x
            cnt += 1
    # 방문 처리 및 큐에 추가
    for j in range(cnt):
        # 범위를 초과하거나 부모 노드가 x가 아니면 잘못된 방문 경로
        if m + j >= N or parent[order[m+j]] != x:
            print(0)
            sys.exit(0)
        # 방문 노드 에 추가 및 방문 체크
        q.append(order[m + j])
        check[order[m + j]] =True
    # 다음 번 검사를 시작할 인덱스
    m += cnt

print(1)