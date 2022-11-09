from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    # 큐 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)                          # queue1 합
    sum2 = sum(queue2)                          # queue2 합
    lenth = (len(queue1) + len(queue2)) * 2     # 반복할 횟수
    cnt = 0                                     # 반복한 횟수
    
    # 각 큐의 합을 비교하며 pop, insert 진행
    while cnt <= lenth:
        # queue2의 합이 더 크면
        if sum1 < sum2:
            tmp = queue2.popleft()  # queue2 pop
            queue1.append(tmp)      # queue1 insert
            sum1 += tmp             # queue1 합에 더하기
            sum2 -= tmp             # queue2 합에서 빼기
        # queue1의 합이 더 크면
        elif sum2 < sum1:
            tmp = queue1.popleft()  # queue1 pop
            queue2.append(tmp)      # queue2 insert
            sum1 -= tmp             # queue1 합에서 빼기
            sum2 += tmp             # queue2 합에 더하기
        # queue1 = queue2면 정답
        else:
            answer = cnt
            break
        # 카운터 증가
        cnt += 1

    return answer