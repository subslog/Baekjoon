from collections import Counter

def n_m(index, N, M):
    # M개의 수열을 뽑으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for i in num:
        a[index] = i         # 수열 넣기
        n_m(index + 1, N, M) # 다음 수열 작업

N, M = map(int, input().split())

# 중복 제거 후 정렬
num = sorted(map(int, set(input().split())))

a = [0] * 9
n_m(0, N, M)