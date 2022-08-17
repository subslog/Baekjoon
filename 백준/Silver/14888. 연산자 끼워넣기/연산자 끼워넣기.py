def next_permutation(a):
    """다음 순열로 변경하는 함수"""
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0: return False

    last_idx = i - 1
    for j in range(last_idx + 1, N - 1):
        if a[last_idx] < a[j]:
            exchange = j

    a[last_idx], a[exchange] = a[exchange], a[last_idx]

    a[last_idx + 1:] = a[-1:last_idx:-1]

    return True

def calc(left: int, right: int, oper: str) -> int:
    """연산 결과 반환 함수"""
    if oper == '+': return left + right
    elif oper == '-': return left - right
    elif oper == '*': return left * right
    else:
        if left >= 0: return left // right
        else: return abs(left) // right * -1

# 정답 저장(최댓값, 최솟값)
answer = [-1000000000, 1000000000]
# 연산자
operator = ['+', '-', '*', '/']
# 초기 입력값
N = int(input())
A = list(map(int, input().split()))
arithmetic = map(int, input().split())
# 연산자로 변환
operators = []
for idx, i in enumerate(arithmetic):
    for j in range(i):
        operators.append(operator[idx])
operators.sort()

while True:
    left_num = A[0]
    # 연산 수행
    for i in range(1, N):
        right_num = A[i]
        left_num = calc(left_num, right_num, operators[i - 1])
    # 최댓값, 최솟값 업데이트
    answer[0] = max(answer[0], left_num)
    answer[1] = min(answer[1], left_num)
    # 다음 순열이 없으면 반복 종료
    if not next_permutation(operators): break

print(answer[0])
print(answer[1])