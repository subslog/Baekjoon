import sys

N = int(input())
answer = [int(sys.stdin.readline()) for _ in range(N)]
answer.sort()

print('\n'.join(map(str, answer)))