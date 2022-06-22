def euclidean(a: int, b: int) -> int:
    """유클리드 호제법"""

    if b == 0:
        return a
    
    return euclidean(b, a % b)

N, S = map(int, input().split())

# 수빈과 각 동생들 사이의 거리
distance = [abs(S - i) for i in map(int, input().split())]

# 동생이 한명이면 거리가 D의 최댓값
if len(distance) == 1:
    D_max = distance[0]
# 첫 번째, 두 번째 동생과의 거리 최대 공약수
else:
    D_max = euclidean(distance[0], distance[1])
# 각 동생들과의 거리에서 최대 공약수 구하기
for i in range(1, len(distance)):
    D_max = euclidean(D_max, distance[i])

print(D_max)