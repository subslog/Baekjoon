import sys

N = int(input())
# 그래프 생성
a = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

# 그래프를 인덱스 기준으로 정렬하기 위한 리스트 생성
b = list(map(lambda x: int(x) - 1, input().split()))
order = [0] * N
for i in range(N):
    order[b[i]] = i

# 인덱스 기준으로 그래프 정렬
for i in range(N):
    a[i].sort(key=lambda x: order[x])

check = [False] * N # 방문 확인용
answer = []         # dfs 저장

def dfs(x: int):
    # 방문 했으면 재귀 종료
    if check[x]: return
    # 방문 처리
    answer.append(x)
    check[x] = True
    # 인접 노드 방문
    for y in a[x]:
        dfs(y)

dfs(0)

for i in range(N):
    # 방문 순서가 다르면
    if answer[i] != b[i]:
        print(0)
        sys.exit(0)
print(1)