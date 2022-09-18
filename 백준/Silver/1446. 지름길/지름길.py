import sys
from collections import deque
INF = int(1e9)

# 초기값 입력
N, D = map(int, input().split())
shortcut = [tuple(map(int, input().split())) for _ in range(N)]
# 지름길 시작 위치 순으로 오름차순 정렬
shortcut.sort()
# 고속도로 길이
road = [i for i in range(D + 1)]

# DP 수행
for i in range(1, D + 1):
    road[i] = road[i - 1] + 1
    # 지름길이 빠르면 업데이트
    for s, e, d in shortcut:
        if s >= 0 and e == i and road[s] + d < road[e]:
            road[e] = road[s] + d

print(road[D])