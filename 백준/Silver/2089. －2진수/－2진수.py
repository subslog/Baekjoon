n = int(input())

answer = ""

if n == 0:
    print(0)
else:
    while n != 1:
        answer += str(n % 2)
        n = -(n // 2)
    answer += str(n)

print(answer[::-1])