import sys

N = int(input())
answer = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    answer.append((int(age), name, i))
answer.sort(key=lambda x:(x[0], x[2]))

for age, name, idx in answer:
    print(age, name)