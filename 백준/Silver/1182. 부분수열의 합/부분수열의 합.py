N, S = map(int, input().split())
a = list(map(int, input().split()))

answer = 0

# 함수 반복
for i in range(1, (1 << N)):
    s = 0
    # 00000 ~ 11111 까지 부분 수열을 더해 S와 같으면 answer +1
    s = sum(a[j] for j in range(N) if i & (1 << j) > 0)
    if S == s: answer += 1

print(answer)