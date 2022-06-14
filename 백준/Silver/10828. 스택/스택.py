import sys

def empty(stack):
    if len(stack):
        return True
    else:
        return False

stack = []

N = int(input())

for _ in range(N):
    commend = sys.stdin.readline().split()

    if commend[0] == "push":
        stack.append(int(commend[1]))
    elif commend[0] == "top":
        if empty(stack):
            print(stack[-1])
        else:
            print(-1)
    elif commend[0] == "pop":
        if empty(stack):
            print(stack.pop())
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(stack))
    elif commend[0] == "empty":
        if empty(stack):
            print(0)
        else:
            print(1)