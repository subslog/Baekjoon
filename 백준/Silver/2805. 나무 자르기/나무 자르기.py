import sys

def tree_cut(arr: list, start: int, end: int, height: int):
    """자른 후 길이 M을 만족하는 절단기의 최대 높이를 반환하는 함수"""
    # start보다 end가 크면 현재 절단기의 최대 높이 반환
    if start > end:
        return height
    mid = (end + start) // 2    # 현재 절단기의 높이
    tree_cnt = 0                # 자른 후 나무의 길이 합
    # 나무의 길이다 절단기의 높이보다 높으면 자른다.
    for tree in arr:
        if tree > mid:
            tree_cnt += tree - mid
    # 자른 나무의 길이 합이 M 미만이면 절단기의 높이를 낮춘다.
    if tree_cnt < M:
        return tree_cut(arr, start, mid - 1, height)
    # 자른 나무의 길이 합이 M 이상이면 절단기의 높이를 높인다.
    else:
        return tree_cut(arr, mid + 1, end, mid)

# 초기값 입력
N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(tree_cut(trees, 0, max(trees), 0))