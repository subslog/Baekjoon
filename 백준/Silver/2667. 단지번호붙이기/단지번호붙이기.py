def dfs(x: int, y: int):
    """dfs로 단지수 카운트하는 함수"""
    # 집이 없으면 재귀 함수 종료
    if a[x][y] == '0': return
    # 집 방문 체크
    a[x][y] = '0'
    # 동일한 단지에서 집 수 카운트
    complex_list[-1] += 1

    # 위 방문
    if x - 1 >= 0: dfs(x - 1, y)
    # 아래 방문
    if x + 1 < N: dfs(x + 1, y)
    # 왼쪽 방문
    if y - 1 >= 0: dfs(x, y - 1)
    # 오른쪽 방문
    if y + 1 < N: dfs(x, y + 1)

N = int(input())

cnt = 0             # 단지 수
complex_list = []   # 단지에 속한 집의 수
a = []              # 그래프 저장 리스트
# 그래프 생성
for i in range(N):
    a.append(list(input()))
# 집 방문하여 단지 확인
for i in range(N):
    for j in range(N):
        # 집이 있으면
        if a[i][j] == '1':
            cnt += 1                # 단지 수 +1
            complex_list.append(0)  # 단지 생성
            dfs(i, j)               # 단지에 있는 집 방문 처리 및 카운트

print(cnt)
print("\n".join(map(str, sorted(complex_list))))