import sys

def ok(idx: int):
    """정답의 조건을 만족하는지 확인하는 함수"""
    s = 0
    for i in range(idx, -1, -1):
        s += answer[i]
        if matrix[i][idx] < 0 and s >= 0: return False
        elif matrix[i][idx] > 0 and s <= 0: return False
        elif matrix[i][idx] == 0 and s != 0: return False
    return True

def go(idx: int):
    """입력된 결과를 만들 수 있는 수열 구하는 함수"""
    if idx == n: return True
    if matrix[idx][idx] == 0:
        answer[idx] = 0
        return ok(idx) and go(idx + 1)
    
    for i in range(1, 11):
        answer[idx] = i * matrix[idx][idx]
        if ok(idx) and go(idx + 1): return True
    
    return False

n = int(input())
result = list(input())
seq = list(range(-10, 11))
c = [False] * 21
answer = [0] * n
matrix = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i, n):
        if result[cnt] == "+": matrix[i][j] = 1
        elif result[cnt] == "-": matrix[i][j] = -1
        else: matrix[i][j] = 0
        cnt += 1

go(0)

print(*answer)