def bulb_change(arr: list, idx: int):
    for i in range(idx, idx + 3):
        if i < N: arr[i] ^= 1

N = int(input())

start = list(map(int, input()))
goal = list(map(int, input()))

# switch[0] : 0 번째 스위치를 누르지 않는 경우
# switch[1] : 0 번째 스위치를 누르는 경우
switch = [start[:], start[:]]
# 0 번째 스위치 누름 처리

switch[1][0] ^= 1
switch[1][1] ^= 1

cnt = [0, 1]
for i in range(N - 1):
    if switch[0][i] != goal[i]:
        bulb_change(switch[0], i)
        cnt[0] += 1
    if switch[1][i] != goal[i]:
        bulb_change(switch[1], i)
        cnt[1] += 1

if switch[0][-1] == switch[1][-1]  == goal[-1]:
    print(min(cnt))
elif switch[0][-1] == goal[-1]:
    print(cnt[0])
elif switch[1][-1] == goal[-1]:
    print(cnt[1])
else:
    print(-1)