A, B, C = map(int, input().split())

net_profit = C - B

if B >= C:
    result = -1
else:
    result = A // net_profit + 1

print(result)