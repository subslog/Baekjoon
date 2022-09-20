from collections import deque

def solution(queue1, queue2):
    answer = -1
    # 목표값
    l_sum = sum(queue1)
    r_sum = sum(queue2)
    # 큐 생성
    q_left = deque(queue1)
    q_right = deque(queue2)

    # 비교 시작
    cnt = 0
    while cnt < len(queue1) * 3:
        # 두 개 큐의 합이 같으면 종료
        if l_sum == r_sum:
            answer = cnt
            break
        # 오른쪽이 크면 왼쪽으로 원소를 넘긴다.
        elif l_sum < r_sum:
            l_sum += q_right[0]
            r_sum -= q_right[0]
            q_left.append(q_right.popleft())
        # 왼쪽이 크면 오른쪽으로 원소를 넘긴다.
        else:
            l_sum -= q_left[0]
            r_sum += q_left[0]
            q_right.append(q_left.popleft())
        cnt += 1
            
    return answer