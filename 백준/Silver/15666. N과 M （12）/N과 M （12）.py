def n_m(index, N, M, start):
    # M개 뽑았으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    for i in range(start, len(num)):
        a[index] = num[i]       # 수열 뽑기
        n_m(index + 1, N, M, i) # 다음 수열 뽑기(현재 수열보다 <=)

N, M = map(int, input().split())
# 중복 제거 후 정렬
num = sorted(map(int, set(input().split())))
# M개 수열 뽑기 체크
a = [0] * 9

n_m(0, N, M, 0)