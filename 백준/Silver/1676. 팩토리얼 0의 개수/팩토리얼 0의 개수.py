import math

N = int(input())

fac = str(math.factorial(N))
answer = 0

for f in fac[::-1]:
    if f == '0':
        answer += 1
    else:
        break

print(answer)