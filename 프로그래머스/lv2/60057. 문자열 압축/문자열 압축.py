def len_check(lenth: int):
    if lenth == 1: return ''
    else: return str(lenth)

def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        stack = []
        string = ''
        # 1 ~ 문자열 길이 / 2 까지 압축
        for j in range(0, len(s), i):
            # 스택이 비었거나 이전 문자와 같으면 push
            if len(stack) == 0 or stack[-1] == s[j:j+i]:
                stack.append(s[j:j+i])
            # 같지 않으면 문자열 연결 후 스택 초기화
            else:
                string += len_check(len(stack)) + stack.pop()
                stack = [s[j:j+i]]

        # 마지막 문자열 처리
        string += len_check(len(stack)) + stack.pop()
        # 최소값 업데이트
        answer = min(answer, len(string))
        
    return answer