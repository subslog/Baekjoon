from collections import deque

def solution(places):
    def bfs(x, y):
        """맨해튼 거리 2 이하에 거리두기 확인 함수"""
        q = deque()         # 방문할 좌표 저장 큐
        q.append((x, y, 0))    # 시작 시점
        cnt = 0             # 맨하튼 거리 계산용
        # 맨해튼 거리 2까지 bfs 수행
        while q:
            x, y, cnt = q.popleft() # 현재 노드
            if cnt >= 2: break      # 맨해튼 거리가 2 이상이면 검사 종료
            check[x][y] = True  # 현재 노드 방문 체크
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]   # 다음 방문할 노드
                # 범위를 벗어나지 않고, 방문하지 않은 노드면 방문
                if 0 <= nx < 5 and 0 <= ny < 5 and not check[nx][ny]:
                    # 현재 노드가 사람 또는 테이블인데 인접 노드가 사람이면 거리두기 위배
                    if place[x][y] in ['P', 'O'] and place[nx][ny] == 'P':
                        return 0
                    q.append((nx, ny, cnt + 1))

        return 1

    # 확인용 상대 좌표(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = [] # 정답 저장
    
    # 모든 강의장 확인
    for place in places:
        # 방문 확인용
        check = [[False] * 5 for _ in range(5)]
        temp = True
        for i in range(5):
            for j in range(5):
                # 사람이면 거리두기 검사
                if place[i][j] == 'P':
                    dist_result = bfs(i, j)
                    # 거리두기 위배
                    if dist_result == 0:
                        temp = False
                        answer.append(0)
                        break
            # 거리두기가 위배됐으면 다음 강의실 검사
            if not temp: break
        else:
            answer.append(1)    # 거리두기 준수
    
    return answer