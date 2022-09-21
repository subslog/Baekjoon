def solution(gems):
    answer = [1, len(gems)]
    # 수집된 보석 저장
    gems_dict = dict()
    # 보석의 수
    gem_cnt = len(set(gems))
    # gems 길이
    lenth = len(gems)
    # 보석 구매
    start, end = 0, 0   # 보석 수집 구간
    result = lenth      # 최소 구간 저장
    while start < lenth and end <= lenth:
        # 모든 보석이 수집되지 않았으면 end 증가
        if len(gems_dict) < gem_cnt:
            if end >= lenth:
                break
            # 수집된 보석이면 수 증가
            if gems[end] in gems_dict:
                gems_dict[gems[end]] += 1
            # 처음 수집되는 보석이면 추가
            else:
                gems_dict[gems[end]] = 1
            end += 1
        # 모든 보석이 수집되면 start 증가
        else:
            # 현재 구간이 짧으면 구간 갱신
            if end - start < result:
                result = end - start
                answer = [start + 1, end]
            # start 위치의 보석의 수가 2개 이상이면 감소
            if gems_dict[gems[start]] > 1:
                gems_dict[gems[start]] -= 1
            # 1개만 있으면 보석 삭제
            else:
                del gems_dict[gems[start]]
            start += 1
            
    return answer