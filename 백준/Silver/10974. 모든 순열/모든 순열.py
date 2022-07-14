def permutation(index: int, N: int):
    # N개의 순열을 뽑았으면 출력 후 재귀 종료
    if index == N:
        print(*a[:index])
        return

    for i in range(1, N + 1):
        if c[i]: continue           # 중복 순열 반복 제외
        c[i] = True                 # 순열 사용
        a[index] = i                # 순열 저장
        permutation(index + 1, N)   # 다음 순열 저장
        c[i] = False                # 순열 사용 끝

N = int(input())

c = [False] * 9 # 중복 순열 체크
a = [0] * 9     # 순열 저장

permutation(0, N)