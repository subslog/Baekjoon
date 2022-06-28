n = int(input())

seq = list(map(int, input().split()))

d = [0] * n     # DP 저장 리스트
d[0] = seq[0]   # 초기값

for i in range(1, n):
    d[i] = seq[i]   # 현재 숫자 저장
    # 이전 숫자가 0보다 크면 더한다.
    if d[i - 1] > 0:
        d[i] += d[i - 1]

print(max(d))