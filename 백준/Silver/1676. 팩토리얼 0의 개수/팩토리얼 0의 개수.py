N = int(input())

i = 5

answer = 0

while i <= N:
    answer += N // i
    i *= 5

print(answer)