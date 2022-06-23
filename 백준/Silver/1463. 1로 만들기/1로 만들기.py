def go(num: int):
    # 1에서 1로 만드는 횟수는 0
    d[1] = 0

    for i in range(2, N + 1):
        # d[i] 를 1로 만드는 최소값 구하기
        d[i] = d[i - 1] + 1
        if i % 2 == 0 and d[i // 2] + 1 < d[i]:
            d[i] = d[i // 2] + 1
        if i % 3 == 0 and d[i // 3] + 1 < d[i]:
            d[i] = d[i // 3] + 1
    
    return d[num]

N = int(input())

d = [0] * (N + 1)

print(go(N))