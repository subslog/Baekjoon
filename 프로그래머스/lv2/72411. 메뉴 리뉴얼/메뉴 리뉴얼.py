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
            group += list(map(lambda x: "".join(x), combinations(sorted(order), cnt)))
        # 만족하는 조합이 없으면 건너뛰기
        if not group: continue
        # 조합 메뉴를 키로 카운트 후 주문순으로 내림차순 정렬
        group = Counter(group).most_common()
        # 2번 이상 시킨 조합이면서 최대값인 조합 모두 추가
        answer += [''.join(i) for i, j in group if j >= 2 and j == group[0][1]]
        
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))