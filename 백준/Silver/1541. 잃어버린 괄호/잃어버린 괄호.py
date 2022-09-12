# 초기값 입력
cal = input()

operand = ['']  # 피연산자
operator = []   # 연산자
for c in cal:
    # 숫자면 피연산자에 리스트에 추가한다.
    if c.isdigit():
        operand[-1] += c
    # 연산자면 연산자 리스트에 추가 및 피연산자 추가
    else:
        operand.append('')
        operator.append(c)     
# 피연산자 int형 변환
operand = list(map(int, operand))
# 마이너스 처음 위치 찾기
minus_idx = len(operand)
for idx, o in enumerate(operator):
    if o == '-':
        minus_idx = idx
        break

# 최소값이 되는 연산 수행
# 마이너스가 나오기 전까지 모두 더하고, 마이너스가 나오면 모두 뺀다.
answer = sum(operand[:minus_idx + 1]) - sum(operand[minus_idx + 1:])
print(answer)