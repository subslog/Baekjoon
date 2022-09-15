def bubble_cnt(arr: list, start: int, end: int):
    """병합 정렬을 수행하면서 swap 횟수 확인"""
    # 1개 요소만 남으면 0 반환
    if start == end:
        return 0
    mid = (start + end) // 2        # 분할
    merge = [0] * (end - start + 1) # 병합할 임시 리스트
    # 왼쪽, 오른쪽 분할
    ans = bubble_cnt(arr, start, mid) + bubble_cnt(arr, mid + 1, end)
    # 병합 시작
    i = start
    j = mid + 1
    k = 0
    while i <= mid or j <= end:
        # 왼쪽 요소가 아직 남은 상태에서 오른쪽에 요소가 없거나 오른쪽 요소보다 작으면 추가
        if i <= mid and (j > end or arr[i] <= arr[j]):
            merge[k] = arr[i]
            k += 1
            i += 1
        # 왼쪽 요소가 없거나 오른쪽 요소가 작으면 추가 및 swap 카운트
        else:
            merge[k] = arr[j]
            k += 1
            j += 1
            ans += (mid - i + 1)
    for i in range(start, end + 1):
        arr[i] = merge[i - start]
    
    return ans


# 초기값 입력
N = int(input())
arr = list(map(int, input().split()))
print(bubble_cnt(arr, 0, N - 1))