def n_m(index, N, M, start):
    # M개 순열을 뽑았으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for i in range(start, N):
        a[index] = prime[i]           # 순열 뽑기
        n_m(index + 1, N, M, i + 1)   # 다음 순열 뽑기(시작 시점 +1)

N, M = map(int, input().split())
prime = sorted(list(map(int, input().split())))

c = [False] * 9 # 중복 순열 체크
a = [0] * 9     # M개 순열 체크

n_m(0, N, M, 0)