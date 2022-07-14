from itertools import product

N, M = map(int, input().split())

# 중복 제거 후 정렬
num = map(str, sorted(map(int, set(input().split()))))
print("\n".join(map(" ".join, product(num, repeat=M))))