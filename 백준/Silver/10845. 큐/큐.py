import sys
import collections

N = int(input())
queue = collections.deque()

for _ in range(N):
    commend = sys.stdin.readline().split()

    if commend[0] == "empty":
        print(0) if queue else print(1)
    elif commend[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "push":
        queue.append(int(commend[1]))
    elif commend[0] == "front":
        print(queue[0]) if queue else print(-1)
    elif commend[0] == "back":
        print(queue[-1]) if queue else print(-1)