postfix = input()

answer = []                             # 정답 저장
stack = []                              # 연산자 저장 스택
priority = {"(":0, "+":1, "-":1, "/":2, "*":2} # 연산자 우선순위

# 후위 표기법 반복
for p in postfix:
    # 피연산자면 answer에 추가
    if p.isalpha():
        answer.append(p)
    # "("면 스택에 push
    elif p == "(":
        stack.append(p)
    # ")"면 "("가 나올 때까지 모든 연산자를 answer에 추가
    elif p == ")":
        while stack[-1] != "(":
            answer.append(stack.pop())
        # ")" 제거
        stack.pop()
    # 연산자면
    else:
        # 우선순위가 낮은 연산자가 나올 때까지 stack에서 pop -> answer에 추가
        while len(stack) and priority[p] <= priority[stack[-1]]:
            answer.append(stack.pop())
        # 현재 연산자 스택에 push
        stack.append(p)
# 스택에 남은 모든 연산자 pop하여 answer에 추가
answer += reversed(stack)

print("".join(answer))