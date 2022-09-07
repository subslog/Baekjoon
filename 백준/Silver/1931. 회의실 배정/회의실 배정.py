N = int(input())
time = [tuple(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
idx = time[0]
for i in range(1, N):
    if idx[1] <= time[i][0]:
        idx = time[i]
        cnt += 1

print(cnt)