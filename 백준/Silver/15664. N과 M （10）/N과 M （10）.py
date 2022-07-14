from collections import Counter

def n_m(index, N, M, start):
    # M개의 수열을 뽑으면 출력 후 재귀 종료
    if index == M:
        print(*a[:index])
        return
    
    for i in range(start, len(num)):
        # 중복 수열이 아니면
        if cnt[i] > 0:
            cnt[i] -= 1             # 중복 체크
            a[index] = num[i]       # 수열 넣기
            n_m(index + 1, N, M, i) # 다음 수열 작업
            cnt[i] += 1             # 중복 해제

N, M = map(int, input().split())

# 수열의 수가 key, 수열의 개수가 value인 dict 생성
tmp = sorted(Counter(list(map(int, input().split()))).items())
# num과 cnt로 분리
num, cnt = map(list, zip(*tmp))

a = [0] * 9
n_m(0, N, M, 0)