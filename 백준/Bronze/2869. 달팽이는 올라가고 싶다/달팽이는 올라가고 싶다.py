import math

A, B, V = map(int, input().split())

# V = A + (A - B) * x 에서 x가 day
# x를 구한다. (A를 먼저 한번 더했으니까 +1)
day = math.ceil((V - A) / (A - B)) + 1

print(day)