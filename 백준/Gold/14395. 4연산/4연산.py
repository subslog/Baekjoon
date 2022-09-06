from collections import deque

def cal(num: int, oper: int):
    """연산 결과 반환 함수"""
    if oper == 0:
        return num * num
    elif oper == 1:
        return num + num
    elif oper == 2:
        return num - num
    elif oper == 3:
        if num == 0:
            return -1
        else:
            return num // num

s, t = map(int, input().split())
oper = ['*', '+', '-', '/']
limit = 1000000000
check = set()

# 시작 숫자 처리
queue = deque([(s, '')])
check.add(s)
# bfs
while queue:
    # 현재 숫자
    num, s = queue.popleft()
    # 목표 숫자를 찾으면 종료
    if num == t:
        # s == t일 경우
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    # *, +, -, / 연산 수행
    for k in range(4):
        next_num = cal(num, k)
        # 범위를 벗어나지 않고, 처리되지 않은 숫자면 처리
        if 0 <= next_num <= limit and next_num not in check:
            check.add(next_num)
            queue.append((next_num, s + oper[k]))
print(-1)