import sys

def division(arr: list, start, end):
    """건물 리스트를 분할하는 함수"""
    # 건물이 1개가 되면 [(L 좌표, 높이), (R 좌표, 0)] 반환
    if start == end:
        return [(arr[start][0], arr[start][1]), (arr[start][2], 0)]
    
    # 분할
    mid = (start + end) // 2
    L = division(arr, start, mid)
    R = division(arr, mid + 1, end)
    # 병합
    return merge(L, R)

def merge(L: list, R: list):
    """분할된 건물을 병합하는 함수"""
    ans = []
    # L, R 건물 높이
    h1, h2 = 0, 0
    # L, R 건물 순서
    i, j = 0, 0
    while i < len(L) and j < len(R):
        # 왼쪽, 오른쪽 건물 (좌표, 높이)
        u, v = L[i], R[j]
        # 좌표 낮은 것부터 추가
        if u[0] < v[0]:
            x = u[0]            # 현재 좌표
            h1 = u[1]           # 현재 높이
            h = max(h1, h2)     # 높은 높이로 사용
            append(ans, (x, h)) # 추가
            i += 1
        else:
            x = v[0]
            h2 = v[1]
            h = max(h1, h2)
            append(ans, (x, h))
            j += 1
    # 남은 건물 처리
    while i < len(L):
        append(ans, L[i])
        i += 1
    while j < len(R):
        append(ans, R[j])
        j += 1
    
    return ans

def append(ans: list, p: tuple):
    """추가되는 건물을 추가하는 함수"""
    if ans:
        # 높이가 같으면 겹치므로 추가할 필요가 없다.
        if ans[-1][1] == p[1]:
            return
        # 위치가 같으면 현재 높이로 업데이트
        if ans[-1][0] == p[0]:
            ans[-1] = (ans[-1][0], p[1])
            return
    ans += [p]



# 초기값 입력
N = int(input())
building = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
building.sort()

for d in division(building, 0, N - 1):
    print(*d, end=' ')