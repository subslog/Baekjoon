def clac(index: int, result: int, plus: int, minus: int, mul: int, div: int):
    """연산자를 조합해 최댓값, 최솟값을 찾는 함수"""
    # 마지막 연산이 끝나면 재귀 종료
    if index == N:
        # 최솟값, 최댓값 갱신
        ans[0] = min(ans[0], result)
        ans[1] = max(ans[1], result)

    # 연산 수행
    if plus > 0:
        clac(index + 1, result + arr[index], plus - 1, minus, mul, div)
    if minus > 0:
        clac(index + 1, result - arr[index], plus, minus - 1, mul, div)
    if mul > 0:
        clac(index + 1, result * arr[index], plus, minus, mul - 1, div)
    if div > 0:
        if result >= 0:
            clac(index + 1, result // arr[index], plus, minus, mul, div - 1)
        else:
            clac(index + 1, abs(result) // arr[index] * -1, plus, minus, mul, div - 1)

N = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
# 최솟값, 최댓값
ans = [1000000000, -1000000000]
clac(1, arr[0], plus, minus, mul, div)

print(ans[1])
print(ans[0])