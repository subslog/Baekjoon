N = int(input())
score = list(map(int, input().split()))
M = max(score)
score_M = sum(score) / M * 100

print(score_M / N)