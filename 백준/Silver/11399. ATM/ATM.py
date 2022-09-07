N = int(input())
time = list(map(int, input().split()))
time.sort()

# 누적합이 되므로 낮은 숫자부터 더해야 한다.
for i in range(1, N):
    time[i] += time[i - 1]

print(sum(time))