from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    # 연산자 종류 찾기
    operator = []
    for o in ['-', '+', '*']:
        search = expression.find(o)
        if search >= 0: operator.append(o)
    # 연산자 우선순위 조합 생성
    operators = permutations(operator)
    # 연산자 분리 후 큐에 저장
    queue_org = deque()
    temp = ''
    for e in expression:
        # 숫자면 문자열 추가
        if e.isdigit():
            temp += e
        # 연산자면 큐에 추가
        else:
            queue_org.append(temp)
            queue_org.append(e)
            temp = ''
    queue_org.append(temp)
    # 우선 순위에 따라 계산 후 최대값 구하기
    for o in operators:
        # 연산용 큐 생성
        queue = queue_org.copy()
        # 1개의 조합 계산
        for i in o:
            result = deque()
            # 큐에 데이터가 없어질 때까지 반복
            while queue:
                # 현재 연산자랑 같으면 계산 후 저장
                if queue[0] == i:
                    queue.popleft()
                    result[-1] = (str(eval(result[-1] + i + queue.popleft())))
                # 현재 연산자가 아니면 그냥 추가
                else:
                    result.append(queue.popleft())
            # 연산 결과로 큐 초기화
            queue = deque(result)
        # 최대값 갱신
        answer = max(answer, abs(int(queue[0])))
        
    return answer