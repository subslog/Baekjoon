def binary_search(arr: list, num: int):
    """정렬된 리스트에서 num이 존재하는지 탐색하는 이진 탐색 함수"""
    l, r = 0, len(arr) - 1
    # 왼쪽 인덱스가 오른쪽 인덱스보다 커질 때까지 반복
    while l <= r:
        mid = (l + r) // 2  # 중간값
        # 찾으면 1 반환
        if arr[mid] == num:
            return 1
        # 찾는 수가 더 작으면 r 업데이트
        elif arr[mid] > num:
            r = mid - 1
        # 찾는 수가 더 크면 l 업데이트
        else:
            l = mid + 1
    # 없는 수면 0 반환
    return 0

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
    answer.append(binary_search(card_list, c))

print(*answer)