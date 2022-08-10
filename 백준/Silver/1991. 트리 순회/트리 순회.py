class Node:
    """트리 저장용 클래스"""
    def __init__(self, left, right):
        self.left = left
        self.right = right
def preorder(x):
    """전위 순회"""
    # 자식 노드가 없으면 순회 종료
    if x == '.': return
    print(x, end='')
    preorder(a[x].left)
    preorder(a[x].right)
def inorder(x):
    """중위 순회"""
    # 자식 노드가 없으면 순회 종료
    if x == '.': return
    inorder(a[x].left)
    print(x, end='')
    inorder(a[x].right)
def postorder(x):
    """후위 순회"""
    # 자식 노드가 없으면 순회 종료
    if x == '.': return
    postorder(a[x].left)
    postorder(a[x].right)
    print(x, end='')

N = int(input())
a = {}
for _ in range(N):
    x, y, z = input().split()
    # 현재 노드에 자식 노드 저장
    a[x] = Node(y, z)

preorder('A')
print()
inorder('A')
print()
postorder('A')