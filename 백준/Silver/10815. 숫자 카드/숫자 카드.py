import bisect
# 초기값 입력
N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

# 카드 리스트 오름차순 정렬
card_list.sort()

# 이진 탐색 수행
answer = []
for c in check_list:
    result = bisect.bisect_right(card_list, c) - bisect.bisect_left(card_list, c)
    # 찾는 카드가 있으면 1, 없으면 0
    if result == 1:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
