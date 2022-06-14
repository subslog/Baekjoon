import sys

N = int(input())

stack = []
last = 0
result = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if last < num:
        for i in range(last + 1, num + 1):
            stack.append(i)
            result.append('+')
        last = num
    elif stack[-1] != num:
        print('NO')
        break
    stack.pop()
    result.append('-')
else:
    print("\n".join(result))