import sys

n = int(input())

triangle = [0]
for _ in range(n):
    triangle.append([0] + list(map(int, sys.stdin.readline().split())))

d = [[0] * (n + 1) for i in range(n + 1)]   # DP 결과 저장 리스트

d[1] = triangle[1] + [0]                    # 초기값

# 점화식 : D[N][i] = N 층에서 합이 최대가 되는 경로에 있는 수의 합
# D[N][i] = max(D[N-1][i-1], D[N-1][i+1]) + triangle[N][i]
for i in range(2, n + 1):
    for j in range(i):
        d[i][j + 1] = max(d[i - 1][j], d[i - 1][j + 1]) + triangle[i][j + 1]
    
print(max(d[n]))