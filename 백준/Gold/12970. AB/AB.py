# 초기값 입력
N, K = map(int, input().split())
# A의 개수를 0 ~ N 개까지 반복
# a: A의 개수, b: B의 개수
# 0 ~ a*b개 까지 조합을 만들 수 있다.
for a in range(0, N + 1):
    b = N - a
    # a*b 보다 큰 K 개의 조합은 만들 수 없다.
    if a * b < K:
        continue
    # 특정 위치에 출력될 A의 개수를 카운트
    cnt = [0] * (b + 1)
    for _ in range(a):
        idx = min(b, K)
        cnt[idx] += 1
        K -= idx
    for i in range(b, 0, -1):
        for _ in range(cnt[i]):
            print('A', end='')
        print('B', end='')
    print()
    exit()
print(-1)