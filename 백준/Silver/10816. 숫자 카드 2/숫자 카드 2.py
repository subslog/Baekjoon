import bisect

# 초기값 입력
N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

# 오름차순 정렬
card_list.sort()

# 이분 탐색을 통해 찾는 카드가 몇 개인지 구한다.
answer = []
for c in check_list:
    # 찾는 카드의 수 = upper bound - lower bound
    cnt = bisect.bisect_right(card_list, c) - bisect.bisect_left(card_list, c)
    answer.append(cnt)

print(*answer)