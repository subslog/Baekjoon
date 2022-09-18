# 초기값 입력
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이진 탐색 수행
start = 0
end = max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2    # 중간값
    tree_cnt = 0                # 자린 나무의 길이
    # 나무의 길이가 절단기 높이보다 길면 자르고 더한다.
    for tree in trees:
        if tree > mid:
            tree_cnt += tree - mid
    # M 개 미만이면 절단기의 높이를 낮춘다.
    if tree_cnt < M:
        end = mid - 1
    # M 개 이상이면 절단기의 높이를 높힌다.
    else:
        answer = mid
        start = mid + 1

print(answer)