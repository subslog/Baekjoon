def solution(stones, k):
    answer = 0
    # 최소, 최대로 건널 수 있는 수로 이분 탐색
    start = 1
    end = max(stones)
    while start <= end:
        # 건널 수 있는지 확인할 최대 인원
        mid = (start + end) // 2

        # 건널 수 있는지 확인
        cnt = 0
        for stone in stones:
            # 건널 수 없는 디딤돌 카운트
            if stone < mid:
                cnt += 1
                # 건널 수 없으면 확인 종료
                if cnt == k:
                    break
            # 건널 수 있으면 초기화
            else:
                cnt = 0

        # 건널 수 있으면 인원을 늘리고, 건널 수 없으면 줄인다.
        if cnt < k:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return answer