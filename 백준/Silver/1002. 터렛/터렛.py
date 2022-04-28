# 원의 방정식 활용

import sys

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    # 두 원의 거리
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 두 원이 완전히 겹치면 경우의 수가 무한대
    if distance == 0 and r1 == r2:
        print(-1)
    # 내접, 외접이면 한점만 겹친다.
    elif r1 + r2 == distance or abs(r1 - r2) == distance:
        print(1)
    # 두 원이 서로 다른 두 점에서 만난다.
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    # 두 원이 만나지 않는 경우
    else:
        print(0)