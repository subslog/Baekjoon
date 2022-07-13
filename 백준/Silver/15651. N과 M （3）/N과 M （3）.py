from itertools import product

N, M = map(int, input().split())

num = map(str, range(1, N + 1))

print("\n".join(list(map(" ".join, product(num, repeat=M)))))