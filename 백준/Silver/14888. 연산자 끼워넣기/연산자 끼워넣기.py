from itertools import permutations
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
operators = ''
for idx, i in enumerate(arithmetic):
    operators += operator[idx] * i
# 연산자 순열 반복
permutation = set(map(''.join, permutations(operators)))
for p in permutation:
    left_num = A[0]
    # 연산 수행
    for i in range(1, N):
        right_num = A[i]
        left_num = calc(left_num, right_num, p[i - 1])
    # 최댓값, 최솟값 업데이트
    answer[0] = max(answer[0], left_num)
    answer[1] = min(answer[1], left_num)

print(answer[0])
print(answer[1])