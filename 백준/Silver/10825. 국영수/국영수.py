import sys

N = int(input())
score = []
for _ in range(N):
    name, korean, english, math = input().split()
    score.append([name, int(korean), int(english), int(math)])

score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in score:
    print(i[0])