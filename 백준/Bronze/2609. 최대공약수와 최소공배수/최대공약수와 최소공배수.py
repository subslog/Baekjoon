def eucliean(a: int, b: int) -> int:
    """유클리드 호제법 함수"""
    if b == 0:
        return a
    else:
        return eucliean(b, a % b)

A, B = map(int, input().split())

answer = eucliean(A, B)

# 최대 공약수
print(answer)
# 최소 공배수
print(int((A * B) / answer))