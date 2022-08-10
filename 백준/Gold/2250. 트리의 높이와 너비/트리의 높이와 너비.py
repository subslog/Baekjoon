class Node:
    """이진 트리 저장 클래스"""
    def __init__(self, left, right):
        self.left = left
        self.right = right
def inorder(x, level):
    """중위 순회"""
    # 자식 노드가 없으면 순회 종료
    if x == -1: return
    # 레벨 키가 사전에 없으면 추가
    if not level in width: width[level] = []

    inorder(a[x].left, level + 1)
    # 노드의 열 번호 증가 후 삽입
    global cnt
    cnt += 1
    width[level].append(cnt)
    inorder(a[x].right, level + 1)
    

N = int(input())
cnt = [0] * (N + 1) # 루트 찾기용
# 그래프 생성
a = [0] * (N + 1)
for _ in range(1, N + 1):
    x, y, z = map(int, input().split())
    a[x] = Node(y, z)
    # 부모가 있으면 카운트
    if y != -1: cnt[y] += 1
    if z != -1: cnt[z] += 1
# 원소값이 0이면 루트
root = 1
for i in range(1, N + 1):
    if cnt[i] == 0: root = i

# 각 레벨의 노드 인덱스 저장용
width = {}
# 너비 카운트
cnt = 0

inorder(root, 1)
level = 1
ans = 0
# 최대 너비 찾기
for i in width:
    if max(width[i]) - min(width[i]) + 1> ans:
        level = i
        ans = max(width[i]) - min(width[i]) + 1

print(level, ans)