import sys

M = int(input())

for i in range(M):
    o_count = 1
    sum = 0
    result = sys.stdin.readline().rstrip()

    for ox in result:
        if ox == 'O':
            sum += o_count
            o_count += 1
        else:
            o_count = 1

    print(sum)