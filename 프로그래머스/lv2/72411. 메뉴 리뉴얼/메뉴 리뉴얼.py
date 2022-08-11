from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # 주문한 갯수를 기준으로 조합 만들기
    for cnt in course:
        group = []
        # 갯수를 기준으로 조합
        for order in orders:
            # 정렬 후 주문 메뉴를 cnt 개로 조합
            group += list(map(lambda x: "".join(x), combinations(sorted(list(order)), cnt)))
        # 만족하는 조합이 없으면 건너뛰기
        if not group: continue
        # 조합 메뉴를 키로 카운트
        group = Counter(group).most_common()
        # 제일 많이 시킨 조합
        max_cnt = max(group, key=lambda x: x[1])[1]
        # 2번 이상 시킨 조합이면서 최대값인 조합 모두 추가
        answer += [i[0] for i in filter(lambda x: x[1] >= 2 and x[1] == max_cnt, group)]
        
    return sorted(answer)