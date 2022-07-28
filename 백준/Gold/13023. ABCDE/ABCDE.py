import sys

N, M = map(int, input().split())

edges = []                                  # 간선 리스트
matrix = [[False] * N for _ in range(N)]    # 인접 행렬
g = [[] for _ in range(N)]                  # 인접 리스트

# A -> B (간선 리스트로 구한다.)
# C -> D (간선 리스트로 구한다.)
# B -> C (인접 행렬로 구한다.)
# D -> E (간접 리스트로 구한다.)
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    # 간선 리스트 삽입
    edges.append((temp[0], temp[1]))
    edges.append((temp[1], temp[0]))
    # 인접 리스트 삽입
    g[temp[0]].append(temp[1])
    g[temp[1]].append(temp[0])
    # 인접 행렬 삽입
    matrix[temp[0]][temp[1]] = matrix[temp[1]][temp[0]] = True

M *= 2  # 간선이 양방향이므로 간선 수 곱하기 2

for i in range(M):
    for j in range(M):
        # A -> B
        A, B = edges[i]
        # C -> D
        C, D = edges[j]
        # 같으면 반복 건너뛰기
        if A == B or A == C or A == D or B == C or B == D or C == D: continue
        # B -> C 없으면 반복 건너뛰기
        if not matrix[B][C]: continue
        # D -> E 구하기
        for E in g[D]:
            # 같으면 반복 건너뛰기
            if A == E or B == E or C == E or D == E:
                continue
            # A -> B -> C -> D -> E 만족
            print(1)
            sys.exit(0)
print(0)