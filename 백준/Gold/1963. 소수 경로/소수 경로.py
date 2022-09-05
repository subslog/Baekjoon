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
# 각 소수에서 한 자리 차이나는 소수 추가
arr = [[] for _ in range(10000)]
for i in range(1000, 10000):
    if prime_check[i]:
        for idx in range(4):
            for n in range(10):
                if idx == 0 and n == 0: continue
                s = list(str(i))
                s[idx] = str(n)
                num = int(''.join(s))
                if i != num and prime_check[num]:
                    arr[i].append(num)

T = int(input())
for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
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
        # 방문하지 않은 숫자는 방문
        for p in arr[b]:
            if dist[p] == -1:
                dist[p] = dist[b] + 1
                queue.append(p)

    if dist[end] == -1:
        print('Impossible')
    else:
        print(dist[end])