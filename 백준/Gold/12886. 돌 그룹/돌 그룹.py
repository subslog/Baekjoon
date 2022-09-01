from collections import deque

def stone(x: int, y: int):
    """돌을 이동하는 함수"""
    # 시작 인덱스 처리
    check[x][y] = True
    queue = deque([(x, y)])
    # bfs
    while queue:
        # 현재 돌의 수
        x, y = queue.popleft()
        now_stone = [x, y, sum - x - y]
        # 모든 돌 확인(X, Y 처리)
        for i in range(3):
            for j in range(3):
                # X, Y가 있고, 처리되지 않은 돌의 개수이면 처리
                if now_stone[i] < now_stone[j]:
                    temp_stone = [x, y, sum - x - y]
                    temp_stone[i] += now_stone[i]
                    temp_stone[j] -= now_stone[i]
                    # 방문하지 않았으면 방문 처리
                    if check[temp_stone[0]][temp_stone[1]] == False:
                        queue.append((temp_stone[0], temp_stone[1]))
                        check[temp_stone[0]][temp_stone[1]] = True

A, B, C = map(int, input().split())
sum = A + B + C
# 돌의 개수를 배열로 체크
check = [[False] * 1501 for _ in range(1501)]

# 3의 배수가 아니면 세 개의 그룹이 같은 개수의 돌을 가질 수 없다.
if sum % 3 != 0:
    print(0)
else:
    stone(A, B)
    # 3으로 나눈 몫의 인덱스가 True이면 세 개 그룹의 돌의 수가 같다.
    if check[sum // 3][sum // 3]:
        print(1)
    else:
        print(0)