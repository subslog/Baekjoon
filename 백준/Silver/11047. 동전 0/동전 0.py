N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0

# 큰 동전부터 사용한다.
for i in A[::-1]:
    cnt += K // i   # 동전으로 나눈 몫이 사용 수
    K %= i          # 남은 돈

print(cnt)