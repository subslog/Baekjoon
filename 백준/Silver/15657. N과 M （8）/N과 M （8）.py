def n_m(index, N, M, start):
    # M개 순열을 뽑았으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for i in range(start, N):
        a[index] = prime[i]     # 순열 뽑기
        n_m(index + 1, N, M, i) # 다음 순열 뽑기(현재 수열 시작부터 시작)

N, M = map(int, input().split())
prime = sorted(list(map(int, input().split())))

a = [0] * 9     # M개 순열 체크

n_m(0, N, M, 0)