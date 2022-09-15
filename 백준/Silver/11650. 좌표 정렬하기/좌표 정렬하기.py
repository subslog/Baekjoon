import sys

N = int(input())
answer = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer.sort()

for i in range(N):
    print(*answer[i])