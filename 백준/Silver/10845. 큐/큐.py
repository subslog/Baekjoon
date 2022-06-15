import sys
import collections

N = int(input())
queue = collections.deque()

for _ in range(N):
    commend = sys.stdin.readline().split()

    if commend[0] == "empty":
        if len(queue):
            print(0)
        else:
            print(1)
    elif commend[0] == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "push":
        queue.append(int(commend[1]))
    elif commend[0] == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)