import heapq

def dijkstra(arr: list, gates: list, summits: list, point: list):
    """start -> 모든 산봉우리의 최소 intensity를 찾는 함수
    : arr: 등산로
    : gates: 등산을 시작할 출입구
    : summits: 목적지
    : point: 출입구, 산봉우리
    """
    # 각 경로로 가는 intensity 무한으로 초기화
    intensity = [int(1e8)] * (len(arr))
    # 모든 출입구를 큐에 넣는다.
    queue = []
    for gate in gates:
        heapq.heappush(queue, (0, gate))
        intensity[gate] = 0

    # 최소 intensity 찾기
    while queue:
        # 현재 비용이 제일 작은 노드
        d, now = heapq.heappop(queue)
        # 이미 방문된 노드 또는 산봉우리면 건너뛴다.
        if intensity[now] < d or point[now] == 1:
            continue
        # 현재 경로와 인접한 경로 확인
        for a in arr[now]:
            # 목적지로 출입구가 나오면 건너뛴다.
            if point[a[1]] == -1: continue
            # 현재 경로를 거쳐 가는 비용이 더 작으면 intensity 갱신
            cost = max(d, a[0])
            if cost < intensity[a[1]]:
                intensity[a[1]] = cost
                heapq.heappush(queue, (cost, a[1]))
    # 최소 intensity를 찾는다.
    min_intensity = [0, int(1e8)]
    for summit in summits:
        if intensity[summit] < min_intensity[1]:
            min_intensity = [summit, intensity[summit]]
    
    return min_intensity

def solution(n, paths, gates, summits):
    # 등산로 생성
    course = [[] for _ in range(n + 1)]
    for s, e, d in paths:
        course[s].append((d, e))
        course[e].append((d, s))
    # 출입구, 산봉우리 확인용
    point = [0] * (n + 1)
    for gate in gates:
        point[gate] = -1
    for summit in summits:
        point[summit] = 1
    # 산봉우리 오름차순 정렬
    summits.sort()
    # 최소 intensity
    answer = dijkstra(course, gates, summits, point)

    return answer