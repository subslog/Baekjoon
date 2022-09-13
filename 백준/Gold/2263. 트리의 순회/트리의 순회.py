import sys
sys.setrecursionlimit(1000000)
# post-order = LR루 순으로 순회하기 때문에 마지막 요소가 무조건 root이다.
# in-order = L루R 순으로 순회하기 때문에 root를 알면 L과 R의 경계를 알 수 있다.
# 확인된 경계의 L과 R로 post-order를 통해 각각의 root를 또 구하면서 반복한다.

def pre_order(in_start: int, in_end: int, post_start: int, post_end : int):
    """in-order와 post-order 정보를 가지고 pre-order를 구하는 함수"""
    # 시작 위치가 종료 위치보다 커지면 종료
    if in_start > in_end or post_start > post_end:
        return
    # post-order에서 root를 찾은 후에 저장하고, in-order에서 root의 위치를 찾는다.
    root = post_order[post_end]
    print(root, end=' ')
    p = in_position[root]

    left = p - in_start
    # 왼쪽 노드 확인
    pre_order(in_start, p - 1, post_start, post_start + left - 1)
    # 오른쪽 노드 확인
    pre_order(p + 1, in_end, post_start + left, post_end - 1)

# 초기값 입력
n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
# in-order 숫자의 인덱스
# root를 그냥 찾으면 시간 복잡도가 O(N**2)이 되기 때문에 위치를 미리 저장해 둔다.
in_position = [0] * (n + 1)
for i in range(n):
    in_position[in_order[i]] = i

# 정답 찾기
pre_order(0, n - 1, 0, n - 1)