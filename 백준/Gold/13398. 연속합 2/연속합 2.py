n = int(input())

seq = [0] + list(map(int, input().split()))

d = [0] * (n + 1)
dr = [0] * (n + 2)

# 왼쪽에서부터 연속합 구하기
for i in range(1, n + 1):
    d[i] = seq[i]
    if d[i] < d[i - 1] + seq[i]:
        d[i] = d[i - 1] + seq[i]
# 오른쪽에서부터 연속합 구하기
for i in range(n, 0, -1):
    dr[i] = seq[i]
    if dr[i] < dr[i + 1] + seq[i]:
        dr[i] = dr[i + 1] + seq[i]

answer = max(d[1:])

# i번 째 수를 제거하여 연속합을 만들어 최대값 계산
for i in range(2, n):
    if answer < d[i - 1] + dr[i + 1]:
        answer = d[i - 1] + dr[i + 1]

print(answer)