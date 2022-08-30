from collections import deque

N, M = map(int, input().split())

dist = [-1] * 101               # 주사위 던진 횟수
next = [i for i in range(101)]  # index칸은 요소 칸으로 이동
# 사다리
for _ in range(N):
    x, y = map(int, input().split())
    next[x] = y
# 뱀
for _ in range(M):
    x, y = map(int, input().split())
    next[x] = y

# 시작 초기값
dist[1] = 0
queue = deque([1])
while queue:
    # 현재 위치
    x = queue.popleft()
    # 주사위 1~6 반복
    for i in range(1, 7):
        y = x + i               # 이동할 칸
        if y > 100: continue    # 100을 넘으면 건너뛴다.
        y = next[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            queue.append(y)

print(dist[100])