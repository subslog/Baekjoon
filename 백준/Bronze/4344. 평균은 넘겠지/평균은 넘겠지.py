import sys

C = int(input())

for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:]) / score[0]
    avg_over_num = 0

    for avg_over in score[1:]:
        if avg_over > avg:
            avg_over_num += 1
    
    print(f'{(avg_over_num / len(score[1:]) * 100):.3f}%')