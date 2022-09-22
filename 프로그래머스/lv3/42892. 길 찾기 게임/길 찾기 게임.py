import sys
sys.setrecursionlimit(100001)

class Node:
    """자식 노드를 저장하기 위한 클래스"""
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    """부모 노드를 저장하기 위한 클래스"""
    def __init__(self, root):
        self.root = root
    
    def insert(self, item):
        self.current_node = self.root
        while True:
            # 현재 노드보다 작다면 왼쪽 노드에 추가
            if item[0] < self.current_node.item[0]:
                # 왼쪽 노드가 있다면 비교 대상을 바꾼다.
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                # 왼쪽 노드가 없다면 추가
                else:
                    self.current_node.left = Node(item)
                    break
            # 현재 노드보다 크다면 오른쪽에 노드 추가
            else:
                # 오른쪽 노드가 있다면 비교 대상을 바꾼다.
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                # 오른쪽 노드가 없다면 추가
                else:
                    self.current_node.right = Node(item)
                    break

def preorder(parend: Node, arr: list):
    """전위 순회 결과를 arr 리스트에 추가"""
    # 자식 노드가 없으면 재귀 종료
    if parend == None:
        return
    # 현재 노드 추가
    arr.append(parend.item[2])
    # 왼쪽 노드 탐색
    preorder(parend.left, arr)
    # 오른쪽 노드 탐색
    preorder(parend.right, arr)

def postorder(parend: Node, arr: list):
    """후위 순회 결과를 arr 리스트에 추가"""
    # 자식 노드가 없으면 재귀 종료
    if parend == None:
        return
    # 왼쪽 노드
    postorder(parend.left, arr)
    # 오른쪽 노드
    postorder(parend.right, arr)
    # 현재 노드 추가
    arr.append(parend.item[2])

def solution(nodeinfo):
    answer = [[], []]
    # 노드 정보에 번호 추가
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    # y를 기준으로 내림차순 정렬
    nodeinfo.sort(key=lambda x: -x[1])
    # 이진 트리 생성
    root = Node(nodeinfo[0])
    tree = BinaryTree(root)
    for i in range(1, len(nodeinfo)):
        tree.insert(nodeinfo[i])

    # 전위 순회
    preorder(tree.root, answer[0])
    # 후위 순회
    postorder(tree.root, answer[1])

    return answer