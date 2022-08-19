def maximum(arr: list, sum: int):
    """최대 에너지 양을 반환하는 함수"""
    global ans
    # 에너지 구슬이 2개 남으면 재귀 종료
    if len(arr) == 2:
        ans = max(ans, sum)
        return
    # 에너지 구슬 사용 재귀
    for i in range(1, len(arr) - 1):
        maximum(arr[:i] + arr[i + 1:], sum + arr[i - 1] * arr[i + 1])

N = int(input())
energy = list(map(int, input().split()))
ans = 0

maximum(energy, 0)

print(ans)