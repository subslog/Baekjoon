from collections import deque
import sys

# 에라토스테네스의 체
prime_check = [True] * 10000
# 루트 9999까지 확인
for i in range(2, int(10000 ** 0.5) + 1):
    # 소수의 배수는 모두 False 처리
    if prime_check[i]:
        for j in range(i + i, 10000, i):
            prime_check[j] = False

T = int(input())
for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    # start ~ end 사이의 소수 리스트 생성
    prime = []
    for i in range(1000, 10000):
        if prime_check[i]:
            prime.append(i)
    # 방문 처리용
    dist = [-1] * 10000
    # 시작 위치 처리
    queue = deque([start])
    dist[start] = 0
    # bfs 수행
    while queue:
        # 현재 숫자
        b = queue.popleft()
        # 목표 소수가 나오면 반복 종료
        if end == b: break
        b1000, b100, b10, b1 = str(b)
        # 소수 자리수 비교
        for p in prime:
            cnt = 0
            p1000, p100, p10, p1 = str(p)
            if b1000 == p1000: cnt += 1
            if b100 == p100: cnt += 1
            if b10 == p10: cnt += 1
            if b1 == p1: cnt += 1
            # 세 자리가 동일하고 방문하지 않았으면 방문
            if cnt == 3 and dist[p] == -1:
                dist[p] = dist[b] + 1
                queue.append(p)

    if dist[end] == -1:
        print('Impossible')
    else:
        print(dist[end])