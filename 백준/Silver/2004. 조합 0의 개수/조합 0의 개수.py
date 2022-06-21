N, M = map(int, input().split())

i = 2
j = 5

two_cnt = 0
five_cnt = 0

# n! 2 개수
while i <= N:
    two_cnt += N // i
    i *= 2
i = 2
# (N - M)! 2 개수
while i <= N - M:
    two_cnt -= (N - M) // i
    i *= 2
i = 2
# M! 2 개수
while i <= M:
    two_cnt -= M // i
    i *= 2

# n! 5 개수
while j <= N:
    five_cnt += N // j
    j *= 5
j = 5
# (N - M)! 5 개수
while j <= N - M:
    five_cnt -= (N - M) // j
    j *= 5
j = 5
# M! 5 개수
while j <= M:
    five_cnt -= M // j
    j *= 5

print(min(two_cnt, five_cnt))