from collections import deque

# 초기값 입력
com_cnt = int(input())
node_cnt = int(input())
# 그래프 생성
graph = [[] for _ in range(com_cnt + 1)]
for _ in range(node_cnt):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)
# 방문 체크
visited = [False] * (com_cnt + 1)

# 시작 노드 처리
queue = deque([1])
visited[1] = True
answer = 0
# bfs를 통해 모든 노드 방문
while queue:
    # 현재 노드
    now = queue.popleft()
    # 인접한 노드 방문:
    for i in graph[now]:
        # 방문하지 않은 노드면 방문
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
            answer += 1

print(answer)