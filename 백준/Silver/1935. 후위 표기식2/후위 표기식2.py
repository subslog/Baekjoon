def calculation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b

import sys

N = int(input())    # 피연산자 수
cal = input()       # 후위 표기식
alpha = {}          # 각 피연산자의 값 저장 딕셔너리
stack = []          # 피연산자 저장 스택

# 피연산자 저장
for i in range(65, 65 + N):
    alpha[chr(i)] = int(sys.stdin.readline())
# 후위 표기식 반복
for c in cal:
    # 알파벳이면
    if c.isalpha():
        # 해당 알파벳의 값 stack에 추가
        stack.append(alpha[c])
    # 알바벳이 아니면
    else:
        # stack에서 요소 2개를 꺼내 해당 연산자로 연산
        temp1 = stack.pop()
        temp2 = stack.pop()
        stack.append(calculation(temp2, temp1, c))

print(f"{stack[0]:.2f}")