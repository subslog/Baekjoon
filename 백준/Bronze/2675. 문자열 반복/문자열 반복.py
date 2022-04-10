import sys

T = int(input())

for _ in range(T):
    R, S = sys.stdin.readline().split()

    # R만큼 반복 출력
    for i in S:
        print(i * int(R), end='')
    
    print() # 줄바꿈