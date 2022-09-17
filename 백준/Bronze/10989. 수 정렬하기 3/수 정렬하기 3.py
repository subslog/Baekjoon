# 카운팅 정렬

import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for i in range(N):
    count[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if count[i]:
        for _ in range(count[i]):
            print(i)
