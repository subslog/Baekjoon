from collections import Counter

def n_m(index, N, M):
    # M개 순열을 뽑았으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for i in range(N):
        # 중복된 수열이면 반복 안하기
        if cnt[i] > 0:
            cnt[i] -= 1             # 중복 순열 처리
            a[index] = num[i]       # 순열 뽑기
            n_m(index + 1, N, M)    # 다음 순열 뽑기
            cnt[i] += 1             # 중복 초기화

N, M = map(int, input().split())
prime = list(map(int, input().split()))
prime = list(Counter(prime).items())    # 요소가 키가 되어 요소의 수만큼 카운트
prime.sort()
N = len(prime)
num, cnt = map(list, zip(*prime))

a = [0] * 9     # M개 순열 체크

n_m(0, N, M)