def position_find(num: str, idx: int, r: int, c: int, lenth: int):
    """사분면 번호의 좌표를 반환하는 함수"""
    # 목표한 위치를 찾으면 반환
    if lenth == 1:
        return (r, c)
    # 현재 존재하는 분면에 따라 다르게 이동한다.
    next_lenth = lenth // 2
    # 제1사분면이면 c 증가한다.
    if num[idx] == '1':
        return position_find(num, idx + 1, r, c + next_lenth, next_lenth)
    # 제2사분면이면 유지한다.
    elif num[idx] == '2':
        return position_find(num, idx + 1, r, c, next_lenth)
    # 제3사분면이면 r 증가한다.
    elif num[idx] == '3':
        return position_find(num, idx + 1, r + next_lenth, c, next_lenth)
    # 제4사분면이면 r, c 증가한다.
    elif num[idx] == '4':
        return position_find(num, idx + 1, r + next_lenth, c + next_lenth, next_lenth)
def num_find(r: int, c: int, lenth: int, dx: int, dy: int):
    """dx, dy 좌표의 사분면 번호를 반환하는 함수"""
    # dx, dy 좌표의 번호를 찾으면 종료
    if lenth == 1:
        return ''
    # 목적지의 분면에 따라 다르게 이동한다.
    next_lenth = lenth // 2
    # 제1사분면이면 c 증가
    if dx < r + next_lenth and dy >= c + next_lenth:
        return '1' + num_find(r, c + next_lenth, next_lenth, dx, dy)
    # 제2사분면이면 유지한다.
    elif dx < r + next_lenth and dy < c + next_lenth:
        return '2' + num_find(r, c, next_lenth, dx, dy)
    # 제3사분면이면 r 증가
    elif dx >= r + next_lenth and dy < c + next_lenth:
        return '3' + num_find(r + next_lenth, c, next_lenth, dx, dy)
    # 제4사분면이면 r, c 증가
    elif dx >= r + next_lenth and dy >= c + next_lenth:
        return '4' + num_find(r + next_lenth, c + next_lenth, next_lenth, dx, dy)

# 초기값 입력
d, num = input().split()
d = int(d)
y, x = map(int, input().split())
# 사분면 제한 크기
size = pow(2, d)
# 목적지 좌표(x는 위가 양수, 아래가 음수이기 때문에 반대로 빼준다.)
dx, dy = position_find(num, 0, 0, 0, size)
dx -= x
dy += y

# 찾는 번호가 범위 안에 있으면 찾고, 없으면 0 반환
if 0 <= dx < size and 0 <= dy < size:
    print(num_find(0, 0, size, dx, dy))
else:
    print(-1)