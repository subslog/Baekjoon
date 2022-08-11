def solution(p):
    answer = ''
    # 빈 문자열이면 빈 문자열 반환
    if not p: return ''

    right = True    # True:올바른, False:균형
    cnt = 0         # 균형잡힌 괄호 판단 카운터
    
    # 괄호 검사
    for i in range(len(p)):
        # '('로 시작하면 올바른 괄호
        if p[i] == '(': cnt += 1
        else: cnt -= 1
        # ')'로 시작해서 균형잡힌 괄호
        if cnt < 0: right = False
        # '(', ')' 수가 동일하면 균형잡힌 괄호
        if cnt == 0:
            # 올바른 괄호면 v 재귀 호출
            if right:
                u = p[:i + 1] + solution(p[i + 1:])
                return u
            # 균형잡힌 괄호면
            else:
                # '()' 사이에 v 재귀 호출
                blank = '(' + solution(p[i + 1:]) + ')'
                # u 앞뒤 괄호 제거 후 뒤집기
                u = ''.join([')' if i == '(' else '(' for i in p[1:i]])
                
                return blank + u