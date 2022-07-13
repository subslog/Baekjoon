def n_m(index, M):
    # M개 순열을 뽑았으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for idx, p in enumerate(prime):
        if c[idx]: continue # 사용한 순열은 반복 넘어가기
        c[idx] = True       # 사용한 순열 체크
        a[index] = p        # 순열 뽑기
        n_m(index + 1, M)   # 다음 순열 뽑기
        c[idx] = False      # 사용한 순열 반납

N, M = map(int, input().split())
prime = sorted(list(map(int, input().split())))

c = [False] * 9 # 중복 순열 체크
a = [0] * 9     # M개 순열 체크

n_m(0, M)