import bisect

# 초기값 입력
N = int(input())
A = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열의 길이 계산
dist = []
lenth = 0
for Ai in A:
    idx = bisect.bisect_left(dist, Ai)
    # 이진 탐색 결과 마지막 인덱스면 새로 추가
    if lenth == idx:
        dist.append(Ai)
        lenth += 1
    # 이진 탐색된 인덱스에 현재의 값으로 업데이트
    # 수열의 길이를 구하는 것이기 때문에 요소가 변경되는 것은 상관없다.
    else:
        dist[idx] = Ai

print(lenth)