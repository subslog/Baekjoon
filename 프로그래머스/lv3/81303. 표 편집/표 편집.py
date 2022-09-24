class Node:
    """연결 리스트용 노드 클래스"""
    def __init__(self, prev = None, next = None):
        """초기화"""
        self.prev = prev    # 리스트의 앞쪽 포인터
        self.next = next    # 리스트의 쥐쪽 포인터

class ArrayLinkedList:
    """연결 리스트 클래스"""
    def __init__(self, capacity: int, k: int):
        """초기화"""
        self.current = k                        # 주목 노드
        self.deleted = []                       # 삭제 데이터
        self.capacity = capacity                # 리스트 크기
        # 리스트 생성
        self.table = []
        for _ in range(self.capacity):
            self.table.append(Node())
        # 첫 번째 노드 삽입
        self.table[0].prev = None
        self.table[0].next = 1
        # 중간 노드 삽입
        for i in range(1, capacity - 1):
            self.table[i].prev = i - 1
            self.table[i].next = i + 1
        # 마지막 노드 삽입
        self.table[capacity - 1].prev = capacity - 2
        self.table[capacity - 1].next = None
    
    def delete(self):
        """주목 노드 삭제"""
        prev_idx = self.table[self.current].prev
        next_idx = self.table[self.current].next
        if prev_idx != None and prev_idx != -1:
            # 앞쪽 노드의 next를 뒤쪽 노드로 변경
            self.table[prev_idx].next = next_idx
        if next_idx != None and next_idx != -1:
            # 뒤쪽 노드의 prev를 앞쪽 노드로 변경
            self.table[next_idx].prev = prev_idx
        # 삭제 처리
        self.deleted.append((self.current, self.table[self.current]))
        self.table[self.current] = -1
        # 뒤쪽 노드가 있으면 주목 노드를 뒤쪽 노드로 변경
        if next_idx:
            self.current = next_idx
        # 뒤쪽 노드가 없으면 주목 노드를 마지막 노드로 변경
        else:
            self.current = prev_idx
    
    def prev(self, X: int):
        """주목 노드를 X 칸 앞으로 이동"""
        for _ in range(X):
            # 첫 번째 노드이면 이동 불가
            if self.table[self.current].prev == None:
                return
            self.current = self.table[self.current].prev
    
    def next(self, X: int):
        """주목 노드를 X 칸 뒤로 이동"""
        for _ in range(X):
            # 마지막 노드이면 이동 불가
            if self.table[self.current].next == None:
                return
            self.current = self.table[self.current].next
    
    def recovery(self):
        """마지막으로 삭제한 노드 복구"""
        idx, recovery_node = self.deleted.pop()
        prev_idx = recovery_node.prev
        next_idx = recovery_node.next
        if prev_idx:
            # 앞쪽 노드의 next를 복구 노드로 변경
            self.table[prev_idx].next = idx
        if next_idx:
            # 뒤쪽 노드의 prev를 복구 노드로 변경
            self.table[next_idx].prev = idx
        # 복구 처리
        self.table[idx] = recovery_node

def solution(n, k, cmd):
    answer = ''
    # 테이블 생성
    table = ArrayLinkedList(n, k)
    # 커맨드 수행
    for c in cmd:
        # X만큼 아래로 이동
        if c[0] == 'D':
            X = int(c.split()[1])
            table.next(X)
        # X만큼 위로 이동
        elif c[0] == 'U':
            X = int(c.split()[1])
            table.prev(X)
        # 주목 노드 삭제
        elif c[0] == 'C':
            table.delete()
        # 마지막 삭제 노드 복구
        else:
            table.recovery()
    # 삭제된 행 확인
    for i in range(n):
        if table.table[i] == -1:
            answer += 'X'
        else:
            answer += 'O'

    return answer