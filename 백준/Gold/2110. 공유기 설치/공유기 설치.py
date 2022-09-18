import sys

# 초기값 입력
N, C = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
# 집 위치 정렬
house.sort()

# 이진 탐색
start, end = 1, house[-1] - house[0]    # 집 사이 간의 최소, 최대 거리
answer = 0                              # 정답
while start <= end:
    # 공유기 설치할 거리
    mid = (start + end) // 2
    # 첫 번째 집에 공유기 설치
    cnt = 1
    last_point = house[0]
    # 공유기를 설치할 수 있는 거리면 설치
    for h in house:
        if h - last_point >= mid:
            cnt += 1
            last_point = h
    # 설치한 공유기가 C 개 미만이면 거리를 좁힌다.
    if cnt < C:
        end = mid - 1
    # 설치한 공유기가 C 개 이상이면 거리를 넓힌다.
    else:
        answer = mid
        start = mid + 1

print(answer)