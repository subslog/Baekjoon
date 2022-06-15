string = input() + "$"  # 끝을 알기위해 $ 추가
bracket_check = 0       # 괄호 체크 변수
stack = ""              # 뒤집을 문자 저장 변수
answer = ""             # 결과 저장 변수

# 입력 문자열 요소 하나씩 반복
for s in string:
    # "<"일 때
    if s == "<":
        # 저장한 stack이 있으면 결과 저장 변수에 추가
        if stack: answer += stack[::-1]
        stack = ""          # stack 초기화
        answer += "<"       # < 추가
        bracket_check = 1   # 괄호 상태 On
        continue
    # ">"일 때
    elif s == ">":
        answer += ">"       # > 추가
        bracket_check = 0   # 괄호 상태 Off
        continue
    # 공백이면
    elif s == " ":
        answer += stack[::-1] + " " # stack 결과 저장 변수에 추가
        stack = ""                  # stack 초기화
        continue
    # 끝 문자면
    elif s == "$":
        answer += stack[::-1]       # stack 결과 저장 변수에 추가
        stack = ""                  # stack 초기화
        break

    # 괄호 상태 On
    if bracket_check:
        answer += s
    # 괄호 상태 Off
    else:
        stack += s

print(answer)