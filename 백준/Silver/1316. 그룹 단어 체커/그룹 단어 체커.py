import sys

N = int(input())

sum = 0

for _ in range(N):
    group_word = sys.stdin.readline().rstrip()
    check = 0
    for i in set(group_word):
        first_index = group_word.find(i)
        last_index = group_word.rfind(i)
        if last_index - first_index + 1 != group_word.count(i):
            break
        check += 1
    if len(set(group_word)) == check:
        sum += 1

print(sum)