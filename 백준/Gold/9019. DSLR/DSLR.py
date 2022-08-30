from collections import deque

def DSLR(num: int, c: str):
    """DSLR의 연산 결과를 반환하는 함수"""
    if c == 'D':
        return (num * 2) % 10000
    elif c == 'S':
        return num - 1 if num - 1 >= 0 else 9999
    elif c == 'L':
        return (num % 1000) * 10 + num // 1000
    elif c == 'R':
        return (num // 10) + (num % 10) * 1000

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    command = [-1] * 10000  # n이 되기 위한 커맨드
    # 시작 초기값
    command[A] = ''
    queue = deque([A])
    # bfs 수행
    while command[B] == -1 and queue:
        # 현재 값
        value = queue.popleft()
        # DSLR 연산 수행
        for i in ['D', 'S', 'L', 'R']:
            result = DSLR(value, i)
            # 아직 계산된 적이 없으면 계산
            if command[result] == -1:
                command[result] = command[value] + i
                queue.append(result)
    
    print(command[B])